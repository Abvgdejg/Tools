import sys
import time

def SetupWriting(self, collection=None):
        self.start_time = time.time()
        self.progression = 0
        self.collection_to_write = collection
    
def WriteConsole(self, title, is_last=False):
    if is_last != True:
        self.progression += 1 

    tmp_time = time.time()
    sys.stdout.write("\r", title, ": ", str(self.progression), \
                    ("/" + str(len(self.collection_to_write)), " " if self.collection_to_write != None else " "), \
                    "(", self.toFixed(self.progression / (tmp_time - self.start_time)), " Frames/s)", ("\n" if is_last else ""))
    sys.stdout.flush()