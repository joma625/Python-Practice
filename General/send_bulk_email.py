#!/usr/bin/env python3

import smtplib, ssl
import os
from dotenv import load_dotenv

# get env var
load_dotenv()
EMAIL = os.environ.get('POSTBAC_EMAIL')
PASS = os.environ.get('POSTBAC_EMAIL_PASS')
RECEIVER = os.environ.get('RECEIVER')

# configuration
port = 465 # for SSL
smtp_server = "smtp.gmail.com"
sender = EMAIL
receiver = RECEIVER
password = PASS
message = """\
Subject: Test

This is a testing email.
This email is sent as a test."""


# create a secure SSL context
context = ssl.create_default_context()
# establish connection and send email
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(EMAIL, PASS)
    server.sendmail(sender, receiver, message)



