### tle data analysis using ephem ###
### being used as module ###
### to predict satellite coordinate for 36 hours ahead ###

# import important modules
import ephem
import datetime
import numpy as np

# function tledata
def tledata(name, line1, line2, date_compute):
    
    # define variables as lists
    waktu_kejadian = []
    longitude = []
    latitude = []
    
    #altitude = []
    
    # define time
    time_zero = datetime.time(0, 0, 0)
    
    date_initial_predict = datetime.datetime.combine(date_compute, time_zero)
    
    # read TLE data into ephem
    tle_rec = ephem.readtle(name, line1, line2)
    
    # for loop to predict satellite coordinate for 36 hours ahead
    # start from now (t=0)
    for t in range(86400):
        
        # interval an hour
        time_delta = datetime.timedelta(seconds=t)
        date_prediction = date_initial_predict + time_delta
        
        
        # compute TLE data
        tle_rec.compute(date_prediction)
        
        # write the data into lists
        waktu_kejadian.append(date_prediction)
        longitude.append(tle_rec.sublong / ephem.degree)
        latitude.append(tle_rec.sublat / ephem.degree)
        #altitude.append(tle_rec.elevation)
    
    waktu_kejadian = np.array(waktu_kejadian)
    longitude = np.array(longitude)
    latitude = np.array(latitude)
    
    index_lower_end = np.argmin(latitude)
    index_upper_end = np.argmax(latitude)
    
    
    if index_lower_end < index_upper_end :
        index_cob_1 = index_lower_end + np.argmin(np.absolute(latitude[index_lower_end:index_upper_end]))
        index_lower_east = index_lower_end + np.argmax(longitude[index_lower_end:index_cob_1])
        index_upper_west = index_cob_1 + np.argmin(longitude[index_cob_1:index_upper_end])
        
        #cari index cob_2
        if np.amin(np.absolute(latitude[0:index_lower_end])) < np.amin(np.absolute(latitude[index_upper_end:-1])) :
            index_cob_2 = np.argmin(np.absolute(latitude[0:index_lower_end]))
        else :
            index_cob_2 = index_upper_end + np.argmin(np.absolute(latitude[index_upper_end:-1]))
        
        #cari yang lain
        if np.amin(longitude[0:index_lower_end]) < np.amin(longitude[index_upper_end:-1]) :
            index_lower_west = np.argmin(longitude[0:index_lower_end])
            
        else :
            index_lower_west = index_upper_end + np.argmin(longitude[index_upper_end:-1])
        
        if np.amax(longitude[0:index_lower_end]) < np.amax(longitude[index_upper_end:-1]) :
            index_upper_east = index_upper_end + np.argmax(longitude[index_upper_end:-1])
            
        else :
            index_upper_east = np.argmax(longitude[0:index_lower_end])
        
    else :
        index_cob_1 = index_upper_end + np.argmin(np.absolute(latitude[index_upper_end:index_lower_end]))
        index_upper_east = index_upper_end + np.argmax(longitude[index_upper_end:index_cob_1])
        index_lower_west = index_cob_1 + np.argmin(longitude[index_cob_1:index_lower_end])
        
        #cari index cob_2
        if np.amin(np.absolute(latitude[0:index_upper_end])) < np.amin(np.absolute(latitude[index_lower_end:-1])) :
            index_cob_2 = np.argmin(np.absolute(latitude[0:index_upper_end]))
        else :
            index_cob_2 = index_lower_end + np.argmin(np.absolute(latitude[index_lower_end:-1]))
        
        #cari yang lain
        if np.amin(longitude[0:index_upper_end]) < np.amin(longitude[index_lower_end:-1]) :
            index_upper_west = np.argmin(longitude[0:index_upper_end])
            
        else :
            index_upper_west = index_lower_end + np.argmin(longitude[index_lower_end:-1])
        
        if np.amax(longitude[0:index_upper_end]) < np.amax(longitude[index_lower_end:-1]) :
            index_lower_east = index_lower_end + np.argmax(longitude[index_lower_end:-1])
            
        else :
            index_lower_east = np.argmax(longitude[0:index_upper_end])
        
        
        
    cob_1 = waktu_kejadian[index_cob_1]
    cob_2 = waktu_kejadian[index_cob_2]
    lower_end = waktu_kejadian[index_lower_end]
    upper_end = waktu_kejadian[index_upper_end]
    
    lower_east = waktu_kejadian[index_lower_east]
    upper_west = waktu_kejadian[index_upper_west]
    upper_east = waktu_kejadian[index_upper_east]
    lower_west = waktu_kejadian[index_lower_west]
    
    
    
    # return dictionary (python) or object (JavaScript)
    return {'cob_1': cob_1, 'cob_2': cob_2, 'upper_end': upper_end, 'lower_end': lower_end, 'lower_east': lower_east, 'upper_west': upper_west, 'lower_west': lower_west, 'upper_east': upper_east}