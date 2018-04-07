#!/usr/bin/python

import time
import os
import smtplib
import mimetypes
import email
import email.mime.application
import sys
from socket import *

def sendMail(IP_Address):
  me = 'rayhallgm@gmail.com'		# Sender's email
  you = 'hallr1@hawkmail.newpaltz.edu'	# Receiver's email
  msg = email.mime.Multipart.MIMEMultipart()
  msg['Subject'] = 'Ray Pi IP Address'
  msg['From'] = me
  msg['To'] = you
  body=email.mime.Text.MIMEText("Assigned IP Address: " + IP_Address + ". Time: " + time.strftime("%Y-%m-%d %H:%M:%S"))
  msg.attach(body)
  clientSocket = smtplib.SMTP('smtp.gmail.com:587')
  clientSocket.starttls()
  clientSocket.login(me,'gsoj fjcy wxdl wzlv')
  clientSocket.sendmail(me,you,msg.as_string())
  clientSocket.quit()
  return

with open("/home/pi/GMAIL/email_IP_log.txt", "a") as outfile:
  trial_date = time.strftime('%m/%d/%y')
  trial_time_start = time.strftime('%H:%M:%S')
  outfile.write('Run date: ' + trial_date + '. Run time: ' + trial_time_start)

  num_exceptions = 0
  not_configured = True
  while(not_configured and num_exceptions < 10):
    try:
      s = socket(AF_INET, SOCK_DGRAM)
      s.connect(("8.8.8.8",80))
      current_IP = s.getsockname()[0]
      s.close()
      sendMail(current_IP)
      not_configured = False
    except:
      num_exceptions += 1
  outfile.write(' Number of exceptions: ' + str(num_exceptions) + '\n')

outfile.close()
