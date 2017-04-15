import requests
import json
import datetime
import pytz
from io import BytesIO
import pycurl

def getTravelInfoNowJson(fromStationID, toStationID, viaStationID='null'):
 now = datetime.datetime.now(pytz.timezone('Europe/Stockholm'))
 buffer = BytesIO()
 c = pycurl.Curl()
 c.setopt(c.URL, 'http://sl.se/api/sv/TravelPlanner/SearchTravelById/null/null/'+str(fromStationID)+'/'+str(toStationID)+'/null/depart/sv/null/'+str(viaStationID)+'/2,8,1,4,/null/null/null/null/null/false/null/1/0/null/true')
 c.setopt(c.WRITEDATA, buffer)
 c.perform()
 c.close()

 body = buffer.getvalue()
 obj = json.loads(body.decode('utf-8'))
 return obj
