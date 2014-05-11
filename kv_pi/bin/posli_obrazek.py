#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Posle na server zadany obrazek. Funguje ve dvou rezimech -- budto
posle posledni snimek z kamery (JPG), anebo GIF animaci.

Pouziti:

    ./posli_obrazek.py <TYP> <CESTA-K-OBRAZKU>
    ./posli_obrazek.py posledni ~/Downloads/tulipan/2014-05-01_1955.jpg

<TYP> je budto "posledni" (cimz se rika ze se posle JPG), nebo
"animace" (cimz se rika ze se posle animovany GIF).
No a <CESTA-K-OBRAZKU> je cesta k obrazku. Asi ne?

Bacha!
Je nutne aby v adresari se skriptem byl soubor settings.py
a v nem uvedeny konfiguracni parametry (vice viz README).
"""

import sys
import os
import requests
from settings import HTTP_TOKEN_NAME, HTTP_TOKEN_VALUE, URL

HEADERS = {HTTP_TOKEN_NAME: HTTP_TOKEN_VALUE}
TYPES = {
    'posledni': 'last.jpg',
    'animace': 'timelapse.gif',
}

if __name__ == '__main__':
    # kontrola parametru
    if len(sys.argv) != 3:
        sys.exit('Zadej typ obrazku a cestu k nemu, napr. "%s posledni ~/camera/2014-05-06_1800.jpg"' % (sys.argv[0], ))

    if sys.argv[1] not in TYPES.keys():
        sys.exit('Jako druhy parametr zadej typ obrazku. Budto "posledni" nebo "animace" (bez uvozovek).')

    filepath = os.path.abspath(os.path.expanduser(sys.argv[2]))
    if not os.path.exists(filepath):
        sys.exit('Zadal jsi neplatnou cestu k obrazku. %s nemuzu najit.' % sys.argv[2])

    # odeslani dat na server
    url = URL + TYPES.get(sys.argv[1])
    files = {'file': open(filepath, 'rb')}
    r = requests.post(url, files=files, headers=HEADERS, timeout=90)
    if r.status_code != 200:
        print r.content
        sys.exit('Obrazek se nepovedlo nahrat na server.')
