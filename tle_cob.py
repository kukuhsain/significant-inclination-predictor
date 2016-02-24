### get TLE data every 15 minutes from celestrak ###
### http://www.celestrak.com/NORAD/elements/geo.txt ###

# import important modules
import time
import ephem_cob as ecob
import urllib2
#import json
import datetime

# get TLE data from celestrak (on-line)


f = open('geo.txt','r')
lines = f.readlines()

    # define satellite
satelit = 'PALAPA C2'

# find the coresponding satellite
for n in range(len(lines)):
    
    if lines[n][0:len(satelit)] == satelit:
        break    

# clean the data
name = lines[n][0:len(satelit)]
line1 = lines[n+1][0:69]
line2 = lines[n+2][0:69]

date_compute = datetime.date.today()

data_prediction = ecob.tledata(name, line1, line2, date_compute)

#show:
print "cob_1"
print data_prediction["cob_1"]

print "cob_2"
print data_prediction["cob_2"]

print "upper_end"
print data_prediction["upper_end"]

print "lower_end"
print data_prediction["lower_end"]
print "\n"
print "\n"
print "lower_east"
print data_prediction["lower_east"]

print "upper_west"
print data_prediction["upper_west"]

print "upper_east"
print data_prediction["upper_east"]

print "lower_west"
print data_prediction["lower_west"]
