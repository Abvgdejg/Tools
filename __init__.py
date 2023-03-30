
#logger = Tools.Logger(log_file, service)
def Logger(log_file, service):
    from . import log 
    logger = log.Logger(log_file, service)
    return logger

#Tools.SpeedTest()
def SpeedTest():
    from . import speedTest as ST
    ST.Load()

#TT = Tools.TimeTools()
def TimeTools():
    from . import timeTools as TT
    tt = TT.TimeTools()
    return tt

def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"