
from django.db.models import Model, CharField, ForeignKey, CASCADE


class Continent(Model):
    name = CharField(max_length=255)


class Country(Model):
    name = CharField(max_length=255)
    continent = ForeignKey(Continent, on_delete=CASCADE)
