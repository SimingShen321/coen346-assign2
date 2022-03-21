import threading
import time
import logging
import readfile
import clock

IDLE = "idle"
ARRIVED = "arrived"
PAUSED = "paused"
RESUMED = "resumed"
FINISHED = "finished"

# 
tempList=[]
   
class Process:
    
    
    def __init__(self, state):
        self.state = state

    
    def getState(self):
        return self.state
        
        
    def setState(self, state):
        self.state = state
        return


    def sortProcess(self):
        tempList= readfile.getwords()
        tempList.sort(key = lambda x: x[1])
        return tempList

    def runTime(self):
        #the run time of each process for 1 cycle
        ranTime= clock.timeSlot(tempList)
        return ranTime
        


    def retrieveProcess(self):
        tempList= readfile.getwords()
        tempList.sort(key = lambda x: x[1])
        def recursiveSearch():
            if tempList[0][1]<clock:
                return 1 + recursiveSearch(tempList[1:])

            elif tempList[0][1] >= clock
                x=tempList[0][1]

                tempList.popleft()
            return x
        return 
   


# x=Process(IDLE)
# x.setState(ARRIVED)
# print(x.getState())
# x.getProcess()

# print(x.processData())  
# p1 = Process(IDLE)
# p1.setState(PAUSED)
# print(p1.getState())