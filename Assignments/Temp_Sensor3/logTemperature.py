#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys

# The function uses a temperature sensor to detect the temperature in degrees
#  Celsius. The temperature is convered to Fahrenheit. Both measurements are
#  returned along with the time of the measurement
def readTemp():
  tempfile = open("/sys/bus/w1/devices/28-000008ab85a7/w1_slave")
  tempfile_text = tempfile.read()
  currentTime = time.strftime('%x %X %Z')
  tempfile.close()
  tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
  tempF=tempC*9.0/5.0+32.0
  return [currentTime, tempC, tempF]

# This function calls readTemp and stores the time and temperature data into
#   a database. 
def logTemperature():
  con = mydb.connect('/home/pi/Assignments/Temp_Sensor3/TempData.db')
  with con:
    try:
      [t,C,F]=readTemp()
      cur = con.cursor()
      cur.execute('insert into TempData values(?,?,?)',(t,C,F))
    except:
      print "Error!!"

logTemperature()
