# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter

from tipi import tipi

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def honzova_typoska(html):
    return tipi(html, lang='cs')
