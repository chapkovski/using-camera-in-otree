from django.contrib.staticfiles.templatetags.staticfiles import static
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import os
import re
import base64
import io
from os import path
from PIL import Image
from django.conf import settings
from uuid import uuid4
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')


class UploadingImagePage(Page):
    form_model = models.Player
    form_fields = ['image_info']

    def before_next_page(self):
        ImageData = self.request.POST.get('image_info')
        ImageData = dataUrlPattern.match(ImageData).group(2)
        i = base64.b64decode(ImageData)
        im = Image.open(io.BytesIO(i))
        # rotate image by 90 degrees
        angle = 90
        out = im.rotate(angle, expand=True)
        your_media_root = settings.MEDIA_ROOT
        file_name = uuid4()
        path_to_file = os.path.join(your_media_root, f'{file_name}.{Constants.IMAGE_EXTENTION}')
        out.save(path_to_file)
        self.player.full_path_to_image = path_to_file
        self.player.image_info = str(file_name)


class Results(Page):
    form_model = models.Player
    form_fields = ['delete_photo']
    def vars_for_template(self):
        return dict()
    def before_next_page(self):
        if self.player.delete_photo:
            self.player._delete_photo()


page_sequence = [
    UploadingImagePage,
    Results
]
