import time
from myscheduler import Priority
import readfile
import threading

#prearrivalQ=[].... this would hole the processes before they arrived 

queue1=[]
queue2=[]

class scheduler:
    
    def timeSlot(self, priority):
        prio = priority       
        timeSlice=0
        
        if prio >100:
            timeSlice=(140-prio)*20
        else:
            timeSlice=(140-prio)*5
    
        return timeSlice




    def runTimeAllocation():


        while True:
                        
            
            if activeQ==0:
                activeQ,expiredQ = expiredQ , activeQ





#boolean flag for active
#q class that inherits q
#override run method
#
#
#
#