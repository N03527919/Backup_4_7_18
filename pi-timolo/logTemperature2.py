#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys
import Adafruit_DHT
import csv

# The function uses a temperature sensor to detect the temperature in degrees
#  Celsius. The temperature is convered to Fahrenheit. Both measurements are
#  returned along with the time of the measurement
def readTemp():
  humidity, temperature = Adafruit_DHT.read_retry(22,4)
  #tempfile = open("/sys/bus/w1/devices/28-000008ab85a7/w1_slave")
  #tempfile_text = tempfile.read()
  currentDate = time.strftime('%x')
  currentTime = time.strftime('%X %Z')
  #tempfile.close()
  #tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
  #tempF=tempC*9.0/5.0+32.0
  temperature = temperature * 9/5.0 + 32
  
  return [currentDate, currentTime, temperature, humidity]

# This function calls readTemp and stores the time and temperature data into
#   a database. 
def logTemperature():
  con = mydb.connect('/home/pi/pi-timolo/project/Data_003.db')
  with con:
    try:
      [d,t,T,h]=readTemp()
      cur = con.cursor()
      cur.execute('insert into TempData values(?,?,?,?)',(d,t,T,h))
    except:
      print "Error!!"

def exportCSV():
   con = mydb.connect('/home/pi/pi-timolo/project/Data_003.db')
   curDB = con.cursor()
   with open('/home/pi/pi-timolo/project/Data_003.csv', 'w') as csvfile:
      writeFile = csv.writer(csvfile, delimiter=',')
      data = curDB.execute('select * from TempData')
      for x in data:
         print x
         writeFile.writerow(x)


logTemperature()
exportCSV()
