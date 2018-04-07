#!/usr/bin/python

# This is a simple script which writes the current
#   time to an output file.

import os
import time
import socket
import gps

# Get GPS information
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
not_found = True # Lat/Lon not yet found
while (not_found):
  try:
    report = session.next()
    if report['class'] == 'TPV':
      if hasattr(report, 'lon'):
        lon = str(report.lon)
        if hasattr(report, 'lat'):
          lat = str(report.lat)
          not_found = False
  except KeyError:
    pass
  except KeyboardInterrupt:
    quit()
  except StopIteration:
    session = None
    print "GPSD has terminated"


currentTime = time.strftime('%x %X %Z')
testString = socket.gethostbyname('raspberrypi')

with open("/home/pi/test.txt", "a") as outfile:
  outfile.write(testString)
  outfile.write('\n')
  outfile.write(lat)
  outfile.write('\n')
  outfile.write(lon)
  outfile.write('\n')

outfile.close()


