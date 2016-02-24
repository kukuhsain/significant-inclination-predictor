### get TLE data every 15 minutes from celestrak ###
### http://www.celestrak.com/NORAD/elements/geo.txt ###

# import important modules
import urllib2
import json

# loop forever
    
data_tle_name = []
data_tle_line1 = []
data_tle_line2 = []

# get TLE data from celestrak (on-line)
f = urllib2.urlopen('http://www.celestrak.com/NORAD/elements/geo.txt')

# read the text data as lines
lines = f.readlines()

for n in range(0,len(lines),3):
    
# clean the data
    name = lines[n]
    line1 = lines[n+1][0:69]
    line2 = lines[n+2][0:69]
    
    name = ' '.join(name.split())
    
    
    data_tle_name.append(name)
    data_tle_line1.append(line1)
    data_tle_line2.append(line2)
    
    
f.close()

with open('js/json/dataTLE.json','w') as f2:
    json.dump(data_tle, f2)
