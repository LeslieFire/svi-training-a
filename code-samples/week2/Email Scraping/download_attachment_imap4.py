'''
Written by Antonio Carlos L. Ortiz 03/06/2015
Input: gmail account
Output: attachments of the results of the specified search criteria from the gmail account
are all saved to one folder called 'detach_dir'
'''



import sys
import imaplib
import email
import datetime
import getpass
import re
import os
from pprin import pprint

detach_dir = 'detach_dir/'

if not os.path.exists(detach_dir[:-1]):
    os.makedirs(detach_dir[:-1])

username = raw_input('Enter your Gmail username: ')
pwd = getpass.getpass('Enter your password: ')

M = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    M.login(username, pwd)
except Exception, e:
    print 'LOGIN FAILED'
    print e

M.select("INBOX", readonly=True)
#for the different search criterias, http://www.example-code.com/csharp/imap-search-critera.asp
#search_response, msg_ids = M.search(None,'UNSEEN','(SUBJECT "foolish consistency")') #searching is not case sensitive
search_response, msg_ids = M.search(None,'(SUBJECT "foolish consistency")')
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

        print mail["From"] + " " + mail["Subject"]

        for part in mail.walk():
            '''
            each part is either non-multipart, or another multipart message
            which constains further parts. Mail is organized like a tree with mail.walk().
            '''
            # multipart parts are just containers so we skip them
            if part.get_content_maintype() == 'multipart':
                continue

            # to check if the part is an attachment. If you want
            if part.get('Content-Disposition') is None:
                continue

            # the same as above
#           if part.get_content_type != 'Content-Disposition':
#                continue

            filename = part.get_filename()
            counter = 1

            # if there is no filename, we create one with a counter to avoid duplicaters
            if not filename:
                filename = 'part-%d' % counter
                counter += 1

            attachment_path = os.path.join(detach_dir, filename)

            #Check if it is already there
            if not os.path.isfile(attachment_path):
                fp = open(attachment_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()