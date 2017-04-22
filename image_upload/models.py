from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as django_models
import random



author = 'Philipp Chapkovski, UZH'

doc = """
The basic usage of camera in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'otreecamera'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    testimage = django_models.TextField()
    delete_photo = models.BooleanField()
