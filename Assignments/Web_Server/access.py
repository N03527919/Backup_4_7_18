#!/usr/bin/python

import sqlite3 as mydb

def getInfo(result):
  print "1"
  print result
  con = mydb.connect('/home/pi/Assignments/Temp_Sensor3/TempData.db')
  with con:
    try:
      cur = con.cursor()
      cur.execute("select * from TempData where date_time>=:start and " \
        "date_time<:end", {"start":start, "end":end})
      output = cur.fetchall()
      return output
    except:
      print "Error!"

