import serial
import time

port = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

rcv = port.read(500)
index = rcv.find("$GPRMC")
start = index + 18
end = start + 1

print rcv

if rcv[start:(start+1)] == "A":	# GPS Data is valid
  print rcv[(start+2):(start+26)]
else:
  print "no"
