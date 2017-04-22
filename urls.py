# urls.py
from django.conf.urls import url
from otree.urls import urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ]

# if settings.DEBUG is True:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns.append(url(r'^my_view/$', 'my_module.my_view'))
