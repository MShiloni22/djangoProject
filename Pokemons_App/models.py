# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pokemons(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    generation = models.IntegerField(db_column='Generation')  # Field name made lowercase.
    legendary = models.BooleanField(db_column='Legendary')  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    attack = models.IntegerField(db_column='Attack')  # Field name made lowercase.
    defense = models.IntegerField(db_column='Defense')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pokemons'
