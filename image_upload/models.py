from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as django_models
import random



author = 'Your name here'

doc = """
Your app description
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
    my_image = django_models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    testimage = django_models.TextField()
