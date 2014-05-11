#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Smaze stare fotky z adresare tak, aby v nich zustaly jen snimky za poslednich
24 hodin. Takto procisteny adresar je pak prichystan, aby se z jeho obsahu
jednoduse udelal animovany GIF reprezentujici vyvoj za poslednich 24 hodin.

Pouziti:
    ./smaz_stare_obrazky.py <CESTA-K-ADRESARI>
    ./smaz_stare_obrazky.py ~/Downloads/tulipan/

<CESTA-K-ADRESARI> je cesta do slozky, kde se ukladaji zmenseniny pro nasledne
vytvoreni animovaneho GIFu.

Poznamka: mechanismus je takovy, ze skript si z nazvu nejcerstvejsiho souboru
zjisti datum jeho vytvoreni, odecte od toho den a vse co je starsi smazne.
"""

import sys
import os
from datetime import datetime, timedelta


if __name__ == '__main__':
    # kontrola parametru
    if len(sys.argv) != 2:
        sys.exit('Zadej cestu do adresare s obrazky, napr. "%s ~/photos/"' % (sys.argv[0], ))

    # je to adresar?
    filepath = os.path.abspath(os.path.expanduser(sys.argv[1]))
    if not os.path.exists(filepath) or not os.path.isdir(filepath):
        sys.exit('Zadal jsi neplatnou cestu k adresari. %s nemuzu najit.' % sys.argv[1])

    # vytahnem si setrideny seznam JPGu
    filenames = sorted([i for i in os.listdir(filepath) if i.endswith('.jpg')])
    if filenames:
        # vytahnem si posledni obrazek a zjistime z nej datum
        last = filenames[-1]
        (date, time) = last.split('_')
        parts = date.split('-')
        # datum o jeden den zpet
        d = datetime(int(parts[0]), int(parts[1]), int(parts[2])) - timedelta(days=1)
        mark = '%s_%s' % (d.strftime('%Y-%m-%d'), time)
        # vsechno co je pred znackou prijde smazat
        to_delete = [i for i in filenames if i <= mark]
        for filename in to_delete:
            os.remove(os.path.join(filepath, filename))
