'''
Written by Antonio Carlos L. Ortiz. Updated: 03/17/2015
Input: gmail account
Output: attachments of the results of the specified search criteria from the gmail account
are all saved to one folder called 'out_dir'
'''
import sys
import imaplib
import email
import datetime
import getpass
import re
import os
from pprint import pprint

out_dir = 'out_dir/'

if not os.path.exists(out_dir[:-1]):
    os.makedirs(out_dir[:-1])

username = raw_input('Enter your Gmail username: ') or 'ortizantoniocarlos@gmail.com'
pwd = getpass.getpass('Enter password for %s: ' % username)

FROM = raw_input('Enter name of sender: ') or 'Crunchbase'
SUBJECT = raw_input('Enter email subject from %s: ' % FROM) or 'News and Startup Events from CrunchBase'
TEXT_TYPE = raw_input('what text type should be returned? (raw or html?): ') or 'html'
TEXT_TYPE = 'text/' + TEXT_TYPE

M = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    M.login(username, pwd)
except Exception, e:
    print 'LOGIN FAILED'
    print e

M.select("INBOX", readonly=True)
#for the different search criterias, http://www.example-code.com/csharp/imap-search-critera.asp
#search_response, msg_ids = M.search(None,'UNSEEN','(SUBJECT "foolish consistency")') #searching is not case sensitive
search_response, msg_ids = M.search(None,'(FROM "%s")' % FROM,'(SUBJECT "%s")' % SUBJECT)
if search_response == 'OK':
    print 'Response Type: ', search_response
    msg_ids = msg_ids[0].split()
    print msg_ids

    for msg_id in msg_ids:
        mail_response, mail_data = M.fetch(msg_id, "RFC822")
        email_body = mail_data[0][1] #email_body is just the raw message
        mail = email.message_from_string(email_body) #parsing the email to get the mail object.

        #if it is not multipart, then the message will only text/plain and no html (i think) or attachments in it.
        if mail.get_content_maintype() != 'multipart':
            continue

        print mail["From"] + " " + mail["Subject"] + " " + mail["Date"]

        count = 0
        for part in mail.walk():
            if part.get_content_type() != TEXT_TYPE:
                continue

            filename = 'Crunchbase Events: %s' % mail["Date"]
            attachment_path = os.path.join(out_dir, filename)

            #Check if the file is already there
            if not os.path.isfile(attachment_path):
                fp = open(attachment_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()