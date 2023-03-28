import time
import sys
import loguru
import os

class WriteTools():

    def __format__(self, __format_spec: str) -> str:
        return str.format(__format_spec)

    start_timer_time = {}

    def toFixed(numObj, digits=2):
        return f"{numObj:.{digits}f}"

    def SetupWriting(collection=None):
        global start_time
        global progression
        global collection_to_write

        start_time = time.time()
        progression = 0
        collection_to_write = collection

    def WriteConsole(title, is_last=False):
        global start_time
        global progression
        global collection_to_write

        if is_last != True:
            progression += 1 

        tmp_time = time.time()
        sys.stdout.write("\r" + title + ": " + str(progression) + ("/" + str(len(collection_to_write)) + " " if collection_to_write != None else " ")  + "(" + toFixed(progression / (tmp_time - start_time)) + " Frames/s)" + ("\n" if is_last else ""))
        sys.stdout.flush()

    def TotalTime(start_time):
        return toFixed(time.time() - start_time)


    def StartTimer(key = 0):
        global start_timer_time

        start_timer_time[key] = time.time()
        
    def ChechTimer(key = 0):

        return toFixed(time.time() - start_timer_time[key])

    def StopTimer(key = 0):

        del start_timer_time[key]

    def anpr(text):
        with open("../logs/log.txt", "a") as log:
            log.write("anpr: " + time.time() + "|" + text)

    def ml(text):
        os.makedirs("../logs", exist_ok=True)
        log = open("../logs/log.txt", "a") 
        log.write(f"ml: {time.time()} | INFO | {text}")

    
