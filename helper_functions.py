# helper functions for CO2 flux calculations   

def get_buoy_locations(): 

    # PMEL open ocean moorings  Carbon Dioxide buoys
    # https://www.pmel.noaa.gov/co2/story/Open+Ocean+Moorings
    # nb: included in s SOCAT data 
    
    buoys = {
        'TAO_110': [0.0, -110.0], 
        'TAO_125': [0.0, -125.0], 
        'TAO_140': [0.0, -140.0], 
        'TAO_155': [0.0, -155.0], 
        'TAO_170': [0.0, -170.0], 
        'TAO_165E':[0.0,  165.0], 
        'TAO_8S': [-8.0,  165.0], 
        'WHOTS':  [22.7, -157.9],
        'STRATUS': [19.6, -85.4], 
        'CCEI':    [33.5, -122.5], 
        'KEO' :    [32.3,  144.5], 
        'PAPA':    [50.1, -144.9], 
        'BOBOA':   [15.0,   90.0], 
        'SOFS':   [-46.8,  142.0], 
        'ICELAND': [68.0,  -12.6],
        'JKEO':    [37.9,  146.6], 
        'BTM':     [31.5,  -65.0], 
        'HALE-ALOHA': [22.8, -158.1],
        'PAP-SO':   [49.0, -16.5], # European, not NOAA
    }
    
    return buoys

#---------------------------------

# Need to map time/lat/lon of data to time/lat/lon of corresponding input products 
# since is sparse data in SOCAT gridded (and likely most other obs products): 
# should either : a) find corresponding time/lat/lon for each observation in each corresponding product  (when not on a single grid) 
# or b) get grid of obs time/lat/lon that can then be mapped to corresponding product grids; and use a lookup/mapping to get corresponding data 

# use b) here:  grid of obs time/lat/lon mapped to corresponding data product 

#-----------------------------------------------


def  get_nearest_index(array, target):
    # finds corresponding nearest coordinate positions in 'target' given elements in 'array'; return size is same as 'array'
    from numpy import asarray, abs
    import numpy as np 
    indexmap = []
    
    array = np.array(array)
    if array.ndim < 1: 
        array = np.array([array])  # cast as a 1-d, not 0-d so can iterate over it 

    for ii in array: 
        indexmap.append(np.abs(ii-target).argmin())
        #indexmap.append(abs(ii-target).argmin())
        
    indexmap = np.asarray(indexmap)
    return(indexmap)



# map indexes from base datasets to corresponding datasets.  maybe is a more elegant way to handle this as xr dataset?  postpone for now.  
# call as:
# x = indexes_map()
# x.lat = get_nearest_index( ds1.lat, ds2.lat ) 
# x.lon = get_nearest_index( ... )


class indexes_map():
    def __init__(self,**kwargs):
        self.Set(**kwargs)
    def Set(self,**kwargs):
        self.__dict__.update(kwargs)
    def SetAttr(self,lab,val):
        self.__dict__[lab] = val

    