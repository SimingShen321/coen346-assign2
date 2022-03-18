import threading
import time
import logging
import readfile

IDLE = "idle"
ARRIVED = "arrived"
PAUSED = "paused"
RESUMED = "resumed"
FINISHED = "finished"


class Process:
    def __init__(self, state):
        self.state = state

    
    def getState(self):
        return self.state
        
        
    def setState(self, state):
        self.state = state
        return
    

    
p1 = Process(IDLE)
p1.setState(PAUSED)
print(p1.getState())
            
    