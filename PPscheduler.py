import time
from myscheduler import Priority
import readfile
import threading
from time import sleep
from collections import deque

#prearrivalQ=[].... this would hole the processes before they arrived 

queue1=[]
queue2=[]

class scheduler(threading.Thread):
    
    def timeSlot(self, priority):
        prio = priority       
        timeSlice=0
        
        if prio >100:
            timeSlice=(140-prio)*20
        else:
            timeSlice=(140-prio)*5
    
        return timeSlice




    def run():

        queue1=True

        while True:

            if :
                #determines the false/true q and sorts elements depending on their priority 


            elif:
                #if there is an element that arrives puts in the false q (expired q)  
                #


            elif queue1 != 0 and  queue1 == True:
                #queue1 manipulate element [0] to do a timeslice 
                # if hte element is paused  then resume
                #queue1.pop[0] 
                
                #do timeslice and pauses PID
                
                
                if queue1.empty():
                    queue1=False
                #empty make it false and q 2 true 

                
                
                #print "Time" + clock + PID + status + "Granted" + time slice      ... or print func idc
                
                sleep(1)




            elif queue2 !=0 and queue2 == True:
                queue2.popleft()   
                
                
                sleep(1)

            

            else:
                break


            
        










#boolean flag for active
#q class that inherits q
#override run method
#
#
#
#