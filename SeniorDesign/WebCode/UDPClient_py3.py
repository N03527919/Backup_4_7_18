#!/usr/bin/python

import os
import time
import gps
import sys
from socket import *

with open("/home/pi/test1.txt", "a") as outfile:
  print ('Log file opened') 
  trial_date = time.strftime('%m/%d/%y')
  trial_time = time.strftime('%H:%M:%S')
  outfile.write('Run date: ' + trial_date + '\n')
  outfile.write('Run time: ' + trial_time + '\n' + '\n')
  start_time = time.time()
  serverName = '192.168.1.168'
  #serverName = '137.140.183.181'
  serverPort = 12001
  
  num_exceptions = 0
  not_configured = True
  while(not_configured):
    try:
      # Try to retrieve the assigned IP address. If no address
      #  is assigned yet, an exception will be thrown. When an
      #  IP address has been assigned, this loop will break.
      clientSocket = socket(AF_INET, SOCK_DGRAM)
      clientSocket.connect(("8.8.8.8", 80))
      outfile.write('Assigned IP Address: ' + clientSocket.getsockname()[0] + '\n')
      clientSocket.close()
      not_configured = False;
      print ('IP Address assigned')
    except:
      num_exceptions += 1
 
  
  outfile.write('Failed attempts to retrieve IP address: ' + str(num_exceptions) + '\n')
  clientSocket = socket(AF_INET, SOCK_DGRAM)
  
  end_time = time.time()
  outfile.write('Program time before IP Address: ' + str(end_time-start_time) + '\n')

  #message = input('Input lowercase sentence:')
  message = 'TROUBLE DETECTED... Acquiring Location...'
  
  try:
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print('Server/Client connection successful')
    #print (modifiedMessage.decode())
  except timeout:
    outfile.write('timeout_error') 
  except gaierror:
    outfile.write('gaierror_error')
  except error:
    outfile.write('error_error')
  except: 
    #outfile.write(msg)
    outfile.write('GPS FAIL!!! ' + str(sys.exc_info()[0]) + '\n')

  # Listen on port 2947 (gpsd) of localhost
  session = gps.gps("localhost", "2947")
  session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

  not_found = True
  while (not_found == True):
    try:
      report = session.next()
      if report['class'] == 'TPV':
        if hasattr(report, 'lon'):
          lon = str(report.lon)
          if hasattr(report, 'lat'):
            lat = str(report.lat)
            not_found = False
            print('GPS location found')
    except KeyError:
      pass
    except KeyboardInterrupt:
      quit()
    except StopIteration:
      session = None
      print ("GPSD has terminated")
    time.sleep(1)
    clientSocket.sendto(message.encode(),(serverName,serverPort))

  final_time = time.time()
  outfile.write('Total program time to send: ' + str(final_time-start_time) + '\n' + '\n')

outfile.close()

message = "Location Retrieved... Lattitude: " + lat +" ... Longitude: " + lon
print (message)
clientSocket.sendto(message.encode(),(serverName,serverPort))

clientSocket.close()
