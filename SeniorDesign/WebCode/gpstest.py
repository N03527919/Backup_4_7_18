#!/usr/bin/python

gpstest = '1'
print gpstest

from socket import *
#serverName = "137.140.183.42"
#serverPort = 12000
#clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket.connect((serverName, serverPort))
#clientSocket.send(gpstest.encode())
#modifiedSentence = clientSocket.recv(1024)
#print("%s: %s" % ("From Server ", modifiedSentence.decode()))

import gps

def main():

   # Listen on port 2947 (gpsd) of localhost
   session = gps.gps("localhost", "2947")
   session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

   while True:
      try:
         report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            #print report
         if report['class'] == 'TPV':
            #print report
            if hasattr(report, 'time'):
               #print report.time
               gpstime = report.time
               print report.time
               print gpstime
               return gpstime 
            #if hasattr(report, 'lon'):
 	    #   print report.lon
            #if hasattr(report, 'lat'):
            #   print report.lat
      except KeyError:
               pass
      except KeyboardInterrupt:
                quit()
      except StopIteration:
               session = None
               print "GPSD has terminated"

if __name__ == "__main__":
   gpstime = main()

serverName = "137.140.183.42"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(gpstime.encode())
modifiedSentence = clientSocket.recv(1024)
print("%s: %s" % ("From Server ", modifiedSentence.decode()))

clientSocket.close()
