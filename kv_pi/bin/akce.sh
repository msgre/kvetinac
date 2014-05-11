#!/bin/bash

BIN_DIR='/home/pi/bin'
PHOTOS_DIR='/home/pi/photos'

# zapnuti svetla
$BIN_DIR/noc.py 20 7
NOC=$?
if [ $NOC -eq 0 ]
  then $BIN_DIR/svetlo.sh 1
fi

# vyfoceni rostlinky
$BIN_DIR/vyfot.sh

# vypnuti svetla
if [ $NOC -eq 0 ]
  then $BIN_DIR/svetlo.sh 0
fi

# kazdou novou fotku hnedle uploadnem na server
cp $PHOTOS_DIR/latest.jpg $PHOTOS_DIR/1500x1125/
mogrify -resize 1500x1125 $PHOTOS_DIR/1500x1125/latest.jpg
$BIN_DIR/posli_obrazek.py posledni $PHOTOS_DIR/1500x1125/latest.jpg
rm $PHOTOS_DIR/1500x1125/latest.jpg

# kazdou celou hodinu vyrobime novy animovany GIF
MINUTE=$(date +"%M")
if [ "$MINUTE" = "50" ]
  then LATEST=`readlink $PHOTOS_DIR/latest.jpg`
       cp $LATEST $PHOTOS_DIR/640x480/
       FILENAME=`basename $LATEST`
       mogrify -resize 640x480 $PHOTOS_DIR/640x480/$FILENAME
       $BIN_DIR/vytvor_gif.sh
fi

# poslem na server info o aktualnich poctech fotek
$BIN_DIR/posli_data.py $PHOTOS_DIR
