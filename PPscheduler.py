import time
from myscheduler import Priority
import readfile
import threading
from time import sleep
from collections import deque
import process
from queue import PriorityQueue
import clock

#prearrivalQ=[].... this would hold the processes before they arrived 

# queue1=[]
# queue2=[]

class scheduler(threading.Thread):

    queue1=[]
    queue2=[]
    
   

    # #def updatePriority(self, priority):

    



    def algo():

        queue1=True

        while True:
            index1=len(queue1)
            index2=len(queue2)

            #check for new process

           
            if  # a new PID is arrived it will be  added  to q in process class but will be handeled here:
               
                

                if queue1 == False:
                    queue1.append(x)
                    
                if queue2 == False:
                    queue2.append(x)
                #if there is an element that arrives puts in the false q (expired q)  
                #organize  the q based on prio


            elif queue1 != 0 and  queue1 == True:
                
                highestPrioProcess= max(queue1, key=lambda item: item[3]) #takes element with highest prio
                
                #x set state either start or resume
                #queue1 manipulate element maxprio element to do a timeslice 
                # if hte element is paused  then resume and update its priority
                #update its state
                #queue1.pop[0] to q2 if not finished pop out to oblivion if done
                #do timeslice and pauses PID
                
                
                if queue1.empty():
                    queue1=False
                    if queue2 != 0:
                        queue2 = True
                #empty make it false and q 2 true 

                
                
                #print "Time" + clock + PID + status + "Granted" + time slice      ... or print func idc
                
                sleep(1)




            elif queue2 !=0 and queue2 == True:
               
               
                highestPrioProcess= max(queue2, key=lambda item: item[3])

                queue2.popleft()   
                
                
                sleep(1)

            

            else:
                break







#q class that inherits q
#override run method
#
#
#
#