#!/usr/bin/python

import smtplib

sender = 'naresheee@gmail.com'
receivers = ['naresheee@gmail.com']

message = """This is test message. Hello friend how are you"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',25)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")