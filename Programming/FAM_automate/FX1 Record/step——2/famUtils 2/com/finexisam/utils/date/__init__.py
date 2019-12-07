from datetime import datetime

def currentString():
    return getDateString(current())
def current():
    result = datetime.now()
    return result;
def getDateString(d,format_str = "%Y-%m-%d_%H-%M-%S"):   
    return datetime.strftime(d,format_str)