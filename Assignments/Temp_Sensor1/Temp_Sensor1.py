#!/usr/bin/python

# The following script uses a temperature sensor to obtain the
#   the current temperature in Celsius. The Fahrenheit temperature
#   is calculated and both are returned along with the current time.

import os
import time
""" Log Current Time, Temperature in Celsius and Fahrenheit
  Returns a list [time, tempC, tempF] """

def readTemp():
   tempfile = open("/sys/bus/w1/devices/28-000008ab85a7/w1_slave")
   tempfile_text = tempfile.read()
   currentTime = time.strftime('%x %X %Z')
   tempfile.close()
   tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
   tempF=tempC*9.0/5.0+32.0
   return [currentTime, tempC, tempF]

print readTemp()
