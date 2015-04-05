'''
Written by Antonio Carlos L. Ortiz. Updated: 04/05/2015
Input: the database query results returned by database_query.py
Output: calls the google calendar api with oauthentication 2.0 and automatically
creates events based from the query.
'''
#!/usr/bin/env python

# modified from:
# https://developers.google.com/api-client-library/python/samples/authorized_api_cmd_line_calendar.py
import httplib2
import sys
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from database_query import query
import json
import collections

def main():

    scope = 'https://www.googleapis.com/auth/calendar'
    
    #flow_from_clientsecrets is better than using OAuth2WebServerFlow.
    #With the former, you only need to state the client_secret json you obtained
    #from the developer console.
    flow = flow_from_clientsecrets('client_secret.json', scope=scope)

    #the 'credentials.dat' is created from the run_flow below.
    storage = Storage('credentials.dat')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        #run_flow is used as opposed to run because the latter is already
        #deprecated.
        credentials = run_flow(flow, storage)

    # Create an httplib2.Http object to handle our HTTP requests, and authorize it
    # using the credentials.authorize() function.
    http = httplib2.Http()
    http = credentials.authorize(http)

    #build is used to create a service object. It takes the API name, the API version.
    #and the http for the credentials.
    service = build(serviceName='calendar',version='v3', http=http)

    event_list = query()
    for event in event_list:
        created_event = service.events().insert(calendarId='primary',body=event).execute()
        pprint(created_event)

if __name__ == '__main__':
    main()

