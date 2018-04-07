#!/usr/bin/python

# The following script accesses a database called 
#   'nyt1.db'. It selects certain data from the 
#   database and prints some of that data to the screen.

import sqlite3 as mydb

con = mydb.connect('nyt1.db')

with con:

  cur = con.cursor()
 
  cur.execute('SELECT Age from nyt1 limit 20')

  data = cur.fetchall()

  print data[0]
  print data[1]



