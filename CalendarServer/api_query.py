"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import eventClass


def query(number):
    # Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=number, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    listOfEvents = [""] * number
    #listOfEvents.setdefault(key, [])
    i = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_date = start[0:10]
        start_time = start[11:16]
        end = event['end'].get('dateTime', event['end'].get('date'))
        end_time = end[11:16]
        listOfEvents[i] = [start_date, start_time,event['summary'], end_time]
        #listOfEvents[i] = (start_date + " " + start_time + " " + event['summary'])
        i += 1
    return listOfEvents

def classTime(today):
    # Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    #listOfEvents = [""] * 10
    #listOfEvents.setdefault(key, [])
    totalTime = 0
    i = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_date = start[0:10]
        start_time = start[11:16]
        end = event['end'].get('dateTime', event['end'].get('date'))
        end_time = end[11:16]
        #end = event['end'].get('dateTime', event['end'].get('date'))
        if start_date == today:
            totalTime += (int(end_time[0:2])-int(start_time[0:2]))*60 + int(end_time[3:5])-int(start_time[3:5])
        #listOfEvents[i] = (start_date + " " + start_time + " " + event['summary'])
        i += 1
    return totalTime
