import threading
import time
import logging
import sched
import readfile

from readfile import getArrivaltime

data = []
data = readfile.getwords()

def sortprocess():
    # sort process by arrival time
    sortByarrival = data
    sortByarrival.sort(key = lambda x: x[1])
    return sortByarrival

print(sortprocess())
    
