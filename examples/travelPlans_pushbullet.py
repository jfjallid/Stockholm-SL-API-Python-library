import sl_api
import datetime
import pytz
from pushbullet import Pushbullet
import yaml
api=""
device=""

with open("config.yaml", 'r') as stream:
    try:
        data = yaml.load(stream) 
        api=data["api"]
        device=data["device"]
    except yaml.YAMLError as exc:
        print(exc)



pb = Pushbullet(api)
msg='---Buss information---\n'
msg= msg + 'Från Norrgårdsvägen till Helenelunds station\n'
msg= msg + 'Beräknat ' + datetime.datetime.now(pytz.timezone('Europe/Stockholm')).strftime('%Y-%m-%d  %H:%M') + "\n"
msg= msg + '---------------------------------------------' + "\n"
count=0

# Example from Norrgårdsvägen (Huddinge) to Helenelund station (Sollentuna)
#obj=sl_api.getTravelInfoNowJson(7061, 9507)

# Example from Norrgårdsvägen (Huddinge) to Södertälje hamn
obj=sl_api.getTravelInfoNowJson(7061, 9521, 9527)
data=obj['data']
for i in obj['data']['Trips']:
  count = count + 1
  msg= msg + '\n--Alt ' + str(count) + ' ank: ' + i['ArrivalTime'] + ' tid: ' + i['Duration'] + '--' + "\n\n"
  for t in i['SubTrips']:
      if t['LineNumber'] != "":
        msg= msg + 'Från ' + t['Origin'] + ' till ' + t['Destination'] + "\n"
        msg= msg + t['TransportText'] + ' avgår kl ' + t['DepartureTime'] + "\n"
msg= msg + '------------------------------'
if device != "":
  print("No device specified. Sending to all devices.")
  lg = pb.get_device(device)
  lg.push_note("SL Trip info", msg)
else:
  pb.push_note("SL Trip info", msg)
