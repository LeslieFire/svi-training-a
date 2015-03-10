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

def main():

    scope = 'https://www.googleapis.com/auth/calendar'
    
    #flow_from_clientsecrets is better than using OAuth2WebServerFlow since
    #with the former, you only need to state the client_secret json you obtained
    #from the developer console.
    flow = flow_from_clientsecrets('client_secret.json', scope=scope)

    #the 'credentials.dat' is created from the run_flow clientsecrets method above.
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

#to list all the events

    print "Upcoming Events:"
    request =  service.events().list(calendarId='primary')
    while request != None:
        #response is a dict of events that are also dicts.
        response = request.execute()
        for event in response.get('items', []):
           print event['summary'], event['start'], event['end'], event.get('location')
        request = service.events().list_next(request, response)

#to post an event
 
    event = {
             'summary':'Appointment',
             'location':'somewhere',
             'start':{
                      'date':'2015-03-15',
             },
             'end':{
                    'date':'2015-03-16',
             },
    }

    created_event = service.events().insert(calendarId='primary',body=event).execute()
    print created_event

if __name__ == '__main__':
    main()

