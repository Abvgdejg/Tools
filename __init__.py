
def Logger(log_file, service):
    from . import log 
    logger = log.Logger(log_file, service)
    return logger

def SpeedTest():
    from . import speedTest as ST
    ST.Load()

def WriteTools():
    from . import writeTools as WT
    wt = WT.WriteTools()
    return wt