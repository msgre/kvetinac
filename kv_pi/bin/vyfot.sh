#!/bin/bash

# Poridi fotku v maximalnim rozliseni a ulozi ji do adresare /home/pi/photos.
# Fotka bude mit jmeno ve tvaru <ROK>-<MESIC>-<DEN>_<HODINA><MINUTA>.jpg.
# Zaroven se v tom samem adresari vytvori symlink "latest.jpg", ktery vede
# vzdy na posledni (nejcerstvejsi) fotku.

DATE=$(date +"%Y-%m-%d_%H%M")
raspistill -n -rot 270 -o /home/pi/photos/$DATE.jpg
ln -sf /home/pi/photos/$DATE.jpg /home/pi/photos/latest.jpg
