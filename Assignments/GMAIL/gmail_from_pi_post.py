#!/usr/bin/python

import time
import os
import smtplib
import mimetypes
import email
import email.mime.application
import sys
from socket import *

def sendMail(ip_address):
  me = 'rayhallgm@gmail.com'		# Sender's email
  you = 'hallr1@hawkmail.newpaltz.edu'	# Receiver's email
  msg = email.mime.Multipart.MIMEMultipart()
  msg['Subject'] = 'Ray Pi IP Address'
  msg['From'] = me
  msg['To'] = you
  body=email.mime.Text.MIMEText("Assigned IP Address: " + ip_address + ". Time: " + time.strftime("%Y-%m-%d %H:%M:%S"))
  msg.attach(body)
  clientSocket = smtplib.SMTP('smtp.gmail.com:587')
  clientSocket.starttls()
  clientSocket.login(me,'gsoj fjcy wxdl wzlv')
  clientSocket.sendmail(me,you,msg.as_string())
  clientSocket.quit()
  return

with open("/home/pi/GMAIL_log3.txt", "a") as outfile:
  trial_date = time.strftime('%m/%d/%y')
  trial_time_start = time.strftime('%H:%M:%S')
  outfile.write('Run date: ' + trial_date + '. Run time: ' + trial_time_start + '\n')

  num_exceptions = 0
  not_configured = True
  while(not_configured and num_exceptions < 1000):
    try:
      s = socket(AF_INET, SOCK_DGRAM)
      s.connect(("8.8.8.8",80))
      ip_address = s.getsockname()[0]
      s.close()
      sendMail(ip_address)
      not_configured = False
    except:
      num_exceptions += 1

outfile.close()
