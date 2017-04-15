# Stockholm-SL-API-Python-library
A simple Python library to get travel information from SL


http://sl.se/api/sv/TravelPlanner/SearchTravelById/"source"/"destination"/"sourceID"/"destinationID"/"time"/"depart_arrive"/sv/null/"via"/"method_of_travel"/"line"/"lines"/"walk_distance"/"changes"/null/"walk_to_other"/null/0/0/null/"realtime"

source: Should be set to null but could specify where you are departing from in text form e.g. Huddinge%20Centrum%20(Huddinge) to include that information in returned JSON object

destination: Should be set to null but could specify your destination in text form e.g. Huddinge%20Centrum%20(Huddinge) to include that information in returned JSON object

sourceID: unique identification of a station or buss stop

destinationID: unique identification of a station or buss stop

time: If the query is for a later point in time you specify the earliest departure time or latest arrival time in the form: 2017-04-16%2012_40 otherwise it should be null

depart_arrive: null if no specific time, otherwise depart for earliest departure time and arrive for latest arrival time

via: stationID of a buss stop or station that should be a subdestination of the trip which could be used to force a route through a specific place.

method_of_travel: list of methods of travel e.g. 8,1,2,4
buss: 8
pendeltåg: 1
tunnelbana: 2
lokalbana: 4

line:
1: lines will list the lines that should not be part of the trip
2: lines will list the only lines that should be part of the trip
null: include all lines

lines: list of lines e.g. 710,744,172 or null if line is null

walk_distance:
200: 200 meter
500: 500 meter
1000: 1km
null: 2km

changes: null if you don't care about number of changes. Otherwise 0, 1, 2 or 3 for max amount of changes.

walk_to_other: false if you don't want to walk to another buss stop or station if it leads to a shorter travel time. true if you don't mind walking

realtime: true if you want realtime and false if you want from timetable