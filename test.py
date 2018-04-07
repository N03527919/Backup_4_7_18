#!/usr/bin/python

#import sys
#import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("8.8.8.8", 80))
#print(s.getsockname()[0])
#s.close()

#num = 0

#with open("/home/pi/test1.txt", "a") as outfile:
#  try:
#    result = 10/0
#
#  except ZeroDivisionError as msg:
#    print(msg)
#    print(str(sys.exc_info()[0]))
#    outfile.write(str(sys.exc_info()[0]))
#
#outfile.close()

import os
import time

with open("/home/pi/test5.txt", "a") as outfile:
   
  counter = 0
  while (counter < 10):
    currentTime = time.strftime('%x %X %Z')
    outfile.write(currentTime)
    outfile.write('\n')
    i = 0
    while (i < 10000):
      i += 1
    counter += 1
    print(currentTime)

outfile.close()

print('done')
