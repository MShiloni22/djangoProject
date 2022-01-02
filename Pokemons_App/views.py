from django.shortcuts import render
from .models import Pokemons


# Create your views here.
def index(request):
    sql = """SELECT *
    FROM Pokemons;
    """
    sql_res = Pokemons.objects.raw(sql)
    return render(request, 'index.html', {'sql_res': sql_res})


def input_processor(request):
    input_text = request.POST['input_text']
    old_word = request.POST['old_word']
    new_word = request.POST['new_word']
    if old_word not in input_text:
        new_input = old_word + " does not appear in the sentence"
        flag = False
    else:
        new_input = input_text.replace(old_word, new_word)
        flag = True
    return render(request, 'input_processor.html', {'new_input': new_input,
                                                    'old_input': input_text,
                                                    'flag': flag})
