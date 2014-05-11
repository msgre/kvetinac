#!/bin/bash

# odstranime z adresare stare fotky
/home/pi/bin/smaz_stare_obrazky.py /home/pi/photos/640x480

# udelame z fotek animovany gif
convert -delay 30 -loop 0 /home/pi/photos/640x480/*.jpg /home/pi/photos/640x480/timelapse.gif

# posleme animovany gif na server
# TODO:
# /home/pi/bin/posli_obrazek.py animace /home/pi/photos/640x480/timelapse.gif
