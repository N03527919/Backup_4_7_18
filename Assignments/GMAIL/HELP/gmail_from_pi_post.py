#!/usr/bin/python

## This script, when executed, sends an email message from your Pi 
## to a specified recipient with a brief message.

## First you must set up 2-step verication with google accounts. Then get an App-specific password  
## that you can use with your Pi. This password is used in the script below.
## See https://support.google.com/accounts/answer/185833?hl=en

import os
#import smtplib
#import mimetypes
#import email
#import email.mime.application
#import sys
import time
#from socket import *

#def sendMail(s, ip_address):
#  me='rayhallgm@gmail.com'  #####Sender's email####
#  you='hallr1@hawkmail.newpaltz.edu'     ### Receiver's email########
#  #another='hallr1@hawkmail.newpaltz.edu'   ### Another recipient ####
#  msg = email.mime.Multipart.MIMEMultipart()
#  msg['Subject'] = 'Test from Pi'
#  msg['From'] = me
#  msg['To'] = you
#  body=email.mime.Text.MIMEText("Assigned IP Address: " + ip_address + ". Time: " + time.strftime("%Y-%m-%d %H:%M:%S"))
#  msg.attach(body)
#  s = smtplib.SMTP('smtp.gmail.com:587')
#  s.starttls()
#  s.login(me,'gsoj fjcy wxdl wzlv') ## Use your App-specific password from google##########
#  #s.sendmail(me,[you,another],msg.as_string())
#  s.sendmail(me,you,msg.as_string())
#  s.quit()
#  return

with open("/home/pi/GMAIL_log.txt", "a") as outfile:
  trial_date = time.strftime('%m/%d/%y')
  trial_time_start = time.strftime('%H:%M:%S')
  outfile.write('Run date: ' + trial_date + '. Run time: ' + trial_time_start + '\n')
  
  #num_exceptions = 0
  #not_configured = True
  #while(not_configured and num_exceptions < 100):
  #  try:
      #s = socket(AF_INET, SOCK_DGRAM)
      #s.connect(("8.8.8.8",80))
      #ip_address = s.getsockname()[0]
      #sendMail(s, ip_address)
      #s.close()
      #trial_time_end = time.strftime('%H:%M:%S')
      #outfile.write('Success at: ' + trial_time_end + '\n')
      #not_configured = False    
  #  except:
  #    num_exceptions += 1

  #if (not_configured):
  #  trial_time_end = time.strftime('%H:%M:%S')
  #  outfile.write('Failed at: ' + trial_time_end + '\n')

outfile.close()

##References
###https://docs.python.org/2/library/email-examples.html
###http://solvingmytechworld.blogspot.com/2013/01/send-email-through-gmail-running-script.html
### http://stackoverflow.com/questions/1966073/how-do-i-send-attachments-using-smtp/8243031#8243031
