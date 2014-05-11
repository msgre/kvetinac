#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Posle na server informaci o tom, kolik se uz nafotilo obrazku.

Pouziti:

    ./posli_data.py <CESTA-DO-ADRESARE>
    ./posli_data.py ~/camera/

<CESTA-DO-ADRESARE> je cesta do adresare! Tam, kde se ukladaji
nasnimane fotky.

Bacha!
Je nutne aby v adresari se skriptem byl soubor settings.py
a v nem uvedeny konfiguracni parametry (vice viz README).
"""

import sys
import os
import requests
import json
from settings import HTTP_TOKEN_NAME, HTTP_TOKEN_VALUE, URL

HEADERS = {HTTP_TOKEN_NAME: HTTP_TOKEN_VALUE}

if __name__ == '__main__':
    # kontrola parametru
    if len(sys.argv) != 2:
        sys.exit('Zadej cestu do adresare s obrazkama, napr. "%s ~/camera/"' % (sys.argv[0], ))

    path = os.path.abspath(os.path.expanduser(sys.argv[1]))
    if not os.path.exists(path) or not os.path.isdir(path):
        sys.exit('Zadal jsi neplatnou cestu k adresari s obrazkama. %s nemuzu najit.' % sys.argv[1])

    # odeslani dat na server
    url = URL + 'data.json'
    filelist = [i for i in os.listdir(path) if i.endswith('.jpg')]
    data = {'photos_count': len(filelist)}
    r = requests.post(url, data=json.dumps(data), headers=HEADERS, timeout=90)
    if r.status_code != 200:
        sys.exit('Data se nepovedlo nahrat na server.')
