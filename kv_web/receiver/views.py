# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime

from PIL import Image

from django.views.generic.base import TemplateView, View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings


class HomeView(TemplateView):
    """
    Homepage.

    Vicemene staticka stranka, do ktere se nalivaji pouze zakladni informace
    z cache (kdy jsme naposledy prijali data a kolik uz je nafoceno fotek).
    """
    template_name = 'bone.html'

    def get_context_data(self):
        out = super(HomeView, self).get_context_data()
        out.update({
            'last_receive': cache.get('last_receive', None),
            'photos_count': cache.get('photos_count', 0),
        })
        return out


class TokenValidatorView(View):
    """
    Pomocne bazove view, ktere proveruje obsah hlavicky -- pokud se v ni
    neobjevuje ocekavana hodnota, odmitne request zpracovat. Jednoducha
    ochrana pred SPAMovanim z vnejsku.
    """

    def post(self, request, *args, **kwargs):
        if request.META.get(settings.HTTP_TOKEN_NAME, None) != settings.HTTP_TOKEN_VALUE or \
           settings.DISABLE_RECEIVING:
            return HttpResponseForbidden()
        return self.process(request, *args, **kwargs)


class ImgReceiverView(TokenValidatorView):
    """
    View, ktere umi prijmout a ulozit 2 typy obrazku -- jpeg s poslednim snimkem,
    a animovany gif za poslednich 24 hodin.

    U JPGu navic dela variantu obrazku, do ktere blendne polopruhlednou vrstvu
    s cernym gradientem na spodnim okraji (takze obrazek prechazi plynule do
    cerne barvy).
    """

    def process(self, request, *args, **kwargs):
        # upload obrazku do docasneho souboru
        temp_filename = kwargs['filename'] + '.temp'
        path = default_storage.save(temp_filename, ContentFile(request.FILES['file'].read()))
        cache.set('last_receive', datetime.now())

        # prejmenovani docasneho souboru na finalni
        temp_filepath = os.path.join(default_storage.location, temp_filename)
        filepath = os.path.join(default_storage.location, kwargs['filename'])
        os.rename(temp_filepath, filepath)

        # vytvoreni gradient varianty
        if kwargs['filename'] == 'last.jpg':
            gradient_filepath = os.path.join(default_storage.location, 'gradient.png')
            original = Image.open(filepath).convert('RGBA')
            gradient = Image.open(gradient_filepath)
            final = Image.alpha_composite(original, gradient)
            final.save(filepath.replace('.jpg', '_gradient.jpg'))

        return HttpResponse('ok')


class DataReceiverView(TokenValidatorView):
    """
    View, ktere prijima JSON metadata popisujici internosti uvnitr Raspberry.
    """

    def process(self, request, *args, **kwargs):
        data = json.loads(request.body)
        cache.set('photos_count', data.get('photos_count', 0))
        return HttpResponse('ok')
