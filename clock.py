from re import L
import time
from myscheduler import Priority
import readfile
import threading
from time import sleep
from collections import deque
import process
from queue import PriorityQueue





def timeSlot(priority=[]):
    prio = int(priority[0][3])       
    timeSlice=0
        
    if prio >100:
        timeSlice=(140-prio)*20
    else:
        timeSlice=(140-prio)*5
    
    return timeSlice






prio = readfile.getwords()
i=readfile.get_num_of_processes()
for x in i:
    del prio[0]
    print(prio[x][1])



def clock():
    
    seconds=timeSlot()
    temporaryClock=seconds
    
    for i in range (seconds):
        seconds-i
        time.sleep(0.1)

