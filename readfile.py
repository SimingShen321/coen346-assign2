from array import *
import functools
import operator
from re import I
def getlines():
    with open("input.txt", "r") as file:
        line = []    
        for i in file:
            stripped_line = i.strip()
            if not i.startswith("#"):
                line.append(i.strip())

        return line
            
def getwords():          
    word = []        
    for i in getlines():
        strippedword = i.split()
        word.append(i.split())
    return word

def get_num_of_processes():
    num = getwords()
    return num[0][0]


def getID():
    flatten = [item for sublist in getwords() for item in sublist]  
    ids = []
    for i in range(1, len(flatten), 4):
        ids.append(flatten[i])  
    return ids
    
def getArrivaltime():
    flatten = [item for sublist in getwords() for item in sublist]  
    arrival = []
    for i in range(2, len(flatten), 4):
        arrival.append(flatten[i])  
    return list(map(int, arrival))

def getBursttime():
    flatten = [item for sublist in getwords() for item in sublist]  
    burst = []
    for i in range(3, len(flatten), 4):
        burst.append(flatten[i]) 
    return list(map(int, burst))
        
def getPriority():
    flatten = [item for sublist in getwords() for item in sublist]  
    initialPriority = []
    for i in range(4, len(flatten), 4):
        initialPriority.append(flatten[i])   
    return list(map(int, initialPriority))
           


    
   

    
                   
        

    



 
