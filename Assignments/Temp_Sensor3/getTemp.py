#!/usr/bin/python

import sqlite3 as mydb

# This script will retrieve tempearture data from the 
#   database named TempData.db

def getTemp():
  con = mydb.connect('/home/pi/Assignments/Temp_Sensor3/TempData.db')
  with con:
    try:
      cur = con.cursor()
      date_start = raw_input("Enter the start date: ")
      print date_start
      date_end = raw_input("Enter the end date: ")
      print date_end
      if (date_end < date_start):
        print "Date Error"
      else:
        cur.execute("select * from TempData where date_time>=:date_start and " \
           "date_time<:date_end", {"date_start": date_start, "date_end": date_end})
        records = cur.fetchall()
        print records
        date = []
        tempC = []
        tempF = []
        for record in records:
          date.append(record[0])
          tempC.append(record[1])
          tempF.append(record[2])
        print "Current date: ", date[2]
        print "Temp C: ", tempC[2]
        print "Temp F: ", tempF[2]
    except:
      print "Error!!"

getTemp()
