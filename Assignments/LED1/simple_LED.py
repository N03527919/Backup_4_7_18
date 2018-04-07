#!/usr/bin/python

# This script will cause an LED to blink 3 times
#   The LED must be connected to GPIO pin #17
#   in series with a resistor to a ground pin

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def Blink():
  for i in range(0,3):
    print "blink #" + str(i+1)
    GPIO.output(17,True)
    time.sleep(1)
    GPIO.output(17,False)
    time.sleep(1)
  print "done!!"
  GPIO.cleanup()
Blink()
