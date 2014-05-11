#!/bin/bash

# Pomocny skript pro ovladani svetla pripojeneho na GPIO4.
# Aby fachal jak ma, tak je treba zajistit 2 veci:
#
# 1) mit inicializovane GPIO; tohle se deje hned pri startu Raspberry,
#    tj. do /etc/rc.local zapsat:
#
#       echo "4" > /sys/class/gpio/export
#       sleep 1
#       echo "out" > /sys/class/gpio/gpio4/direction
#
# 2) Volat tento skript s parametrem 0 nebo 1. Hodnota 0 svetlo vypina,
#    hodnota 1 zapina. Tj. napr.:
#
#       ./svetlo.sh 0   # svetlo se vypne
#       ./svetlo.sh 1   # svetlo se zapne

echo $1 > /sys/class/gpio/gpio4/value
