import httplib2
import sys

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

client_id = "626863754731-7kit8dtv8trrhjbtcjunvr19i58sb5u1.apps.googleusercontent.com"
client_secret = "oFoce5HGsyt6CUSP5UG17U2s"

# The URL for read/write access to a user's calendar data
scope = 'https://www.googleapis.com/auth/calendar'

# The flow object holds the client_id, client_secret, and scope
flow = OAuth2WebServerFlow(client_id, client_secret, scope)

def main():

  # Create a Storage object. This object holds the credentials that your application needs to authorize access to the user's data
  storage = Storage('credentials.dat')

  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

  # Create an httplib2.Http object to handle our HTTP requests, and authorize it using the credentials.authorize() function.
  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('calendar', 'v3', http=http)

  try:

    request = service.events().list(calendarId='primary')
    # Loop until all pages have been processed.
    while request != None:
      # Get the next page.
      response = request.execute()
      # Accessing the response like a dict object with an 'items' key
      # returns a list of item objects (events).
      for event in response.get('items', []):
        # The event object is a dict object with a 'summary' key.
        print (repr(event.get('summary', 'NO SUMMARY')) + '\n')

      request = service.events().list_next(request, response)

  except AccessTokenRefreshError:
    # The AccessTokenRefreshError exception is raised if the credentials
    # have been revoked by the user or they have expired.
    print ('The credentials have been revoked or expired, please re-run'
           'the application to re-authorize')

if __name__ == '__main__':
  main()