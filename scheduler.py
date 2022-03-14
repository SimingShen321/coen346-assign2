from hashlib import new
import time
import readfile

class Priority:
    
    
    def processData(self, no_of_processes):
        process_data = []
        
        for i in range(int(readfile.get_num_of_processes())):
            temporary = []
            
            pid = []
            pid = readfile.getID()
            process_id = pid[i]
            
            arvl = []
            arvl = readfile.getArrivaltime()
            arrival_time = arvl[i]
            
            brst = []
            brst = readfile.getBursttime()
            burst_time = brst[i]
            
            prio = []
            prio = readfile.getPriority()
            priority = prio[i]
            
            temporary.extend([process_id, arrival_time, burst_time, priority, 0, burst_time])
            
            process_data.append(temporary)
            print(process_data)
        Priority.schedulingProces(self, process_data)





            