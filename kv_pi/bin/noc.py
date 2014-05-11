#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pomocny skript na vyhodnoceni, jestli je den nebo noc (a jestli se
behem foceni ma zapinat baterka nebo ne).

Pouziti:

    ./tma.py <OD> <DO>
    ./tma.py 20:00 6:30

Parametry <OD> <DO> rikaji, odkdy dokdy je tma. Po spusteni skriptu
si zjisti aktualni cas, a pokud se vleze do zadaneho intervalu, vrati
navratovou hodnotu 0. V opacnem pripade vraci 1.

Poznamka: rozpoznani navratove hodnoty v BASHi se da udelat takto:

    ~/bin/noc.py 20 7
    RET=$?                      # v promenne $RET se ulozi navratova hodnota z noc.py
    if [ $RET -eq 0 ]           # test na hodnotu 0
      then ~/bin/svetlo.sh 1    # reakce na hodnotu 0
    fi
"""

import sys
from datetime import datetime, time

def parse_time(val):
    """
    Pomocna funkce, ktera ze zadaneho retezce ve tvaru "6" ci
    "20:45" udela objekt time() se zadanym casem. Pokud by sem
    prisel nejaky nesmysl (treba "sdkjfls" nebo "56:99"), tak
    vrati None.
    """
    parts = val.split(':')
    if len(parts) == 1:
        parts.append('0')
    elif len(parts) != 2:
        return None

    parts = [int(i) for i in parts if i.isdigit()]
    if len(parts) != 2:
        return None

    try:
        out = time(parts[0], parts[1])
    except:
        return None
    return out


if __name__ == '__main__':
    # kontrola parametru
    if len(sys.argv) != 3:
        sys.exit('Zadej cas odkdy dokdy si myslis, ze je tma, napr. "%s 20:30 05:30"' % (sys.argv[0], ))

    time_from = parse_time(sys.argv[1])
    time_to = parse_time(sys.argv[2])
    if time_from is None:
        sys.exit('Chybny format casu od: %s. Zadej ho ve tvaru HH:MM, napr. 20:30.' % (sys.argv[1], ))
    if time_to is None:
        sys.exit('Chybny format casu do: %s. Zadej ho ve tvaru HH:MM, napr. 06:20.' % (sys.argv[2], ))

    # tak co? je den nebo noc?
    now = datetime.now()
    if now.time() > time_from or now.time() < time_to:
        # je tma!
        sys.exit()

    # je den
    sys.exit(1)
