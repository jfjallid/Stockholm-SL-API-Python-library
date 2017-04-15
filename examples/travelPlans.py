import sl_api
import datetime
import pytz

print ('---Buss information---')
print ('Från Norrgårdsvägen till Helenelunds station')
print ('Beräkningar från ' + datetime.datetime.now(pytz.timezone('Europe/Stockholm')).strftime('%Y-%m-%d  %H:%M'))
print ('----------------------')
print()
count=0

# Example from Norrgårdsvägen (Huddinge) to Helenelund station (Sollentuna)
#obj=sl_api.getTravelInfoNowJson(7061, 9507)

# Example from Norrgårdsvägen (Huddinge) to Södertälje hamn
obj=sl_api.getTravelInfoNowJson(7061, 9521, 9527)
data=obj['data']
for i in obj['data']['Trips']:
 count = count + 1
 print ('--- Alt ' + str(count) + ' ankomst ' + i['ArrivalTime'] + ' restid: ' + i['Duration'] + ' ---')
 for t in i['SubTrips']:
     if t['LineNumber'] != "":
       print ('Från ' + t['Origin'] + ' till ' + t['Destination'])
       print(t['TransportText'] + ' avgår kl ' + t['DepartureTime'] )
       print()
print ('------------------------------')
