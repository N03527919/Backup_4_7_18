#!/usr/bin/python

import sqlite3 as mydb

date = "2017-03-25"
print date

out_date = date.split("-")
print out_date[0]

date = out_date[1] + "/" + out_date[2] + "/" + out_date[0][-2:]

print date

con = mydb.connect('/home/pi/Assignments/Temp_Sensor3/TempData.db')
with con:
  cur = con.cursor()
  cur.execute("SELECT * FROM TempData WHERE date_time>=:date",{"date":date})
  records = cur.fetchall()
  date = []
  tempC = []
  tempF = []
  for record in records:
    date.append(record[0])
    tempC.append(record[1])
    tempF.append(record[2])
  print date
