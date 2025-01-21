from peewee import *

db = SqliteDatabase('./db/football_mcda.db')

class Player(Model):
    name = CharField()
    skill = IntegerField()
    pace = IntegerField()
    strength = IntegerField()
    age = IntegerField()
    cost = IntegerField()

    class Meta:
        database = db