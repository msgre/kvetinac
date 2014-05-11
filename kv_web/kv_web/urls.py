# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from receiver.views import HomeView, ImgReceiverView, DataReceiverView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^prijem/(?P<filename>timelapse\.gif|last\.jpg)$', csrf_exempt(ImgReceiverView.as_view()), name='img-receiver'),
    url(r'^prijem/data.json$', csrf_exempt(DataReceiverView.as_view()), name='data-receiver'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
