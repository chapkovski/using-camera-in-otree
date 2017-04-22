from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import os
import re
import base64
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
from django.contrib.staticfiles.templatetags.staticfiles import static


class UploadingImagePage(Page):
    form_model = models.Player
    form_fields = ['testimage']


    def before_next_page(self):
        ImageData = self.request.POST.get('testimage')
        ImageData = dataUrlPattern.match(ImageData).group(2)

        # If none or len 0, means illegal image data
        if (ImageData == None or len(ImageData) == 0):
            # PRINT ERROR MESSAGE HERE
            pass

        # Decode the 64 bit string into 32 bit
        ImageData = base64.b64decode(ImageData)
        print(ImageData)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path_to_file = os.path.join(BASE_DIR, 'static/image_upload/photo{}.jpg'.format(self.participant.code))
        f = open(path_to_file, 'wb' )
        f.write( ImageData)
        f.close()

class Results(Page):
    form_model = models.Player
    form_fields = ['delete_photo']

    def vars_for_template(self):
        return {'myphoto':'image_upload/photo{}.jpg'.format(self.participant.code)}

    def before_next_page(self):
        if self.player.delete_photo:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            path_to_file = os.path.join(BASE_DIR, 'static/image_upload/photo{}.jpg'.format(self.participant.code))
            os.remove(path_to_file)


page_sequence = [
    UploadingImagePage,
    Results
]
