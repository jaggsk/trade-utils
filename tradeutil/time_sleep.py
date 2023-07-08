import datetime
import time
import enum
import math

class time_sleep_calculator:

    '''
    (datetime string)(string)->(integer)
    A class to calculate interval in seconds between the last API GET time csall or local system request
    and a predetermined interval (in seconds)
    PRECONDITIONS - Input timedata is supplied in the correct format
    KJAGGS NOV 2022
    
    '''
    def __init__(self):
        #instantiate class
        print("Instantiate time sleep period calculator")

    def time_sleep(self, time_stamp, interval = '5min') :
        
        #extract hour, minute and second from datetime object
        #print(time_stamp.hour,time_stamp.minute,time_stamp.second)
        self.time_stamp_hour = time_stamp.hour
        self.time_stamp_minute = time_stamp.minute
        self.time_stamp_second = time_stamp.second
        
        #calculate the raemainging seconds to the next specified time interval
        #5min interval, 1->5,13->15, 49->50 etc
        if interval == '1min':    
            self.time_interval = 60
            self.time_sleep_final = self.time_interval - time_stamp.second

        elif interval == '5min':    
            self.time_interval = 300
            rnd_int = self.round_up_integer(self.time_stamp_minute,5)
            self.time_sleep_final = ((rnd_int-time_stamp.minute)*60)-time_stamp.second

        elif interval == '15min':    
            self.time_interval = 900
            rnd_int = self.round_up_integer(self.time_stamp_minute,15)
            self.time_sleep_final = ((rnd_int-time_stamp.minute)*60)-time_stamp.second
    
        elif interval == '30min':    
            self.time_interval = 1800
            rnd_int = self.round_up_integer(self.time_stamp_minute,30)
            self.time_sleep_final = ((rnd_int-time_stamp.minute)*60)-time_stamp.second

        elif interval == '1hr':    
            self.time_interval = 3600
            rnd_int = self.round_up_integer(self.time_stamp_minute,60)
            self.time_sleep_final = ((rnd_int-time_stamp.minute)*60)-time_stamp.second

        elif interval == '4hr':    
            self.time_interval = 14400
            rnd_int = self.round_up_integer(self.time_stamp_hour,4)
            self.time_sleep_final = ((rnd_int-time_stamp.hour)*3600)-(time_stamp.minute*60)-time_stamp.second

        elif interval == '1d':    
            self.time_interval = 86400   
            rnd_int = self.round_up_integer(self.time_stamp_hour,24)  
            self.time_sleep_final = ((rnd_int-time_stamp.hour)*3600)-(time_stamp.minute*60)-time_stamp.second


    def round_up_integer(self, n, base):
        '''
        (int)(int)->(int)
        rounds an integer up to next specified base multiple.
        e.g. n = 12, base = 5, return = 15
        '''

        if n%base == 0:
            return int(math.ceil(n/base)*base)+base
        else:
            return int(math.ceil(n/base)*base)
    


