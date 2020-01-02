#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:49:36 2020

@author: sunil
"""

import panads
import time
import imaplib
import smtplib
import email
from email.parser import BytesParser
#from imaginary import magic_html_parser

ORG_MAIL = "@gmail.com"
MY_EMAIL =  #Put your email ID
FROM_MAIL = MY_EMAIL+ORG_MAIL
PWD = #put your email pwd (key is two stage verification is on)
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_MAIL,PWD)
mail.select('inbox')
type,data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()
first_email_id = id_list[0]
latest_email_id = id_list[-1]

type, data = mail.fetch(latest_email_id, '(RFC822)')

for response in data:
    if isinstance(response,tuple):
        msg = email.message_from_string(response[1].decode('ISO-8859-1'))
        email_from = msg['from']
        email_to = msg['to']
        subject = msg['subject']


for part in msg.walk():
    body = part.get_payload(decode = True)
    
    
    file_name = "email_" + '1' + ".txt"
    output_file = open(file_name, 'w')
    output_file.write("From: %s\nTo: %s\nSubject: %s\n\nBody: \n\n%s" %(email_from, email_to, subject, body))
    output_file.close()
