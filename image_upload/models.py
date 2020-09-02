from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels
import random
import os

author = 'Philipp Chapkovski, HSE-Moscow'

doc = """
The basic usage of camera in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'otreecamera'
    players_per_group = None
    num_rounds = 1
    IMAGE_EXTENTION = 'png'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    full_path_to_image = models.LongStringField()
    image_info = models.LongStringField()
    delete_photo = models.BooleanField()

    def _delete_photo(self):
        os.remove(self.full_path_to_image)
