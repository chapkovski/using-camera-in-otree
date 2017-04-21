from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random

class MyBot(Bot):
    myprop = 666
    def __init__(self,*args,**kwargs):
        # print('IPORTANT!!!!',dir(self))
        self.myprop = random.random()
        # print('*********************', self.myprop)
        super(MyBot, self).__init__(*args,**kwargs)




class PlayerBot(MyBot):

    def play_round(self):
        # print('^^^^^^^^^^^^^^', self.myprop, 'RRRR',self.player.round_number)
        print('ROUNDDDD',self.player.participant.vars['myrand'], '$$$$$$', self.player.participant.code)
        yield (views.Demographics, {'age': 3, 'gender': 'Male'})
