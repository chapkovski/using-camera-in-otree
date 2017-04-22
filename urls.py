# urls.py
from django.conf.urls import url
from otree.urls import urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from image_upload import gallery



urlpatterns.append(url(r'^gallery/$', 'image_upload.gallery.gallery'))
