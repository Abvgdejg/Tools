import time
from . import toFixed

class TimeTools():

    start_timer_time = {}

    def TotalTime(self, start_time):
        return toFixed(time.time() - start_time)

    def StartTimer(self, key = 0):
        self.start_timer_time[key] = time.time()
        
    def ChechTimer(self, key = 0):
        return toFixed(time.time() - self.start_timer_time[key])

    def StopTimer(self, key = 0):
        del self.start_timer_time[key]

    
