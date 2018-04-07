#!/usr/bin/python
# -*- coding: utf-8 -*-

#####https://docs.python.org/2/library/sqlite3.html###########

# The following script function prints the version of SQLite
#   which is installed on the operating system. It then prints
#   the current date and time.

import sqlite3 as mydb
import sys
import time

con = mydb.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data

def readTime():
  currentDate = time.strftime("%Y/%m/%d")
  currentTime = time.strftime("%H:%M:%S")
  return [currentDate, currentTime] 

print readTime()
