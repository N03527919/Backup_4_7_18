#!/usr/bin/python
import serial

ser = serial.Serial("/dev/ttyS0",9600,timeout=1)
info = ser.read(5)
print info
