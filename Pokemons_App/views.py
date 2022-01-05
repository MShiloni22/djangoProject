# Create your views here.
from django.shortcuts import render
from .models import Pokemons
from datetime import datetime
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    dic = {}
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def index(request):
    return render(request, 'index.html')

def new_file(request):
    return render(request, 'new_file.html')

def query_results(request):
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT Generation, Name 
        FROM (SELECT p.Generation AS Gen, MAX(p.ATTACK + p.DEFENSE + p.HP) AS TOTAL
        FROM Pokemons p
        GROUP BY Generation) AS strongest INNER JOIN Pokemons p1 ON strongest.Gen = p1.Generation
        WHERE Legendary=1 AND (ATTACK + DEFENSE + HP) = TOTAL
        ORDER BY Generation;
        """)
        sql_res1 = dictfetchall(cursor)

        cursor.execute("""
        select type, name from Pokemons P
        except
        select P1.type, P1.name
        from Pokemons P1 join Pokemons P2 on P1.Type=P2.Type
        WHERE ((p2.HP >= p1.HP or p2.Attack >= p1.Attack or p2.Defense >= p1.Defense) and p2.Name != p1.Name)
        order by Type
        """)
        sql_res2 = dictfetchall(cursor)

        sql_res3 = {}
        if request.method == 'POST' and request.POST:
            threshold = request.POST["X"]
            count = request.POST["Y"]
            cursor.execute(f"""
                            SELECT p.Type 
                            FROM Pokemons p
                            GROUP BY p.Type
                            HAVING COUNT(*) > {count}
                            EXCEPT (SELECT p1.Type 
                                    FROM Pokemons p1
                                    GROUP BY p1.Type
                                    HAVING MAX(p1.Attack) <= {threshold});
                                    """)
            sql_res3 = dictfetchall(cursor)

        cursor.execute("""
        select top 1 AvgInstbByType.Type, AvgInstbByType.Instability from (
            select type, round(avg(sub),2) as instability from (
                select type, cast(abs(Defense - Attack) as float) as sub from Pokemons
                ) as InstbByPokemon
                group by type)
            as AvgInstbByType
        order by instability desc
        """)
        sql_res4 = dictfetchall(cursor)

        return render(request, 'query_results.html', {'sql_res1': sql_res1,
                                                      'sql_res2': sql_res2,
                                                      'sql_res3': sql_res3,
                                                      'sql_res4': sql_res4})
