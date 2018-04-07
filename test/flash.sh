#!/bin/bash
#  Short script to toggle a GPIO pin at the highest frequency possible

echo 4 > /sys/class/gpio/export
sleep 0.5
echo "out" > /sys/class/gpio/gpio4/direction
COUNTER=0
while [ $COUNTER -lt 100000 ]; do
   echo 1 > /sys/class/gpio/gpio4/value
   let COUNTER=COUNTER+1
   echo 0 > /sys/class/gpio/gpio4/value
done
echo 4 > /sys/class/gpio/unexport
