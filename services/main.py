#!/usr/bin/python3

with open("/home/pi/test1.txt", "a") as outfile:
  outfile.write('hello')
  outfile.write('\n')
outfile.close()


