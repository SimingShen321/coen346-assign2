import time
import readfile


class Priority:
    
    def processData(self, no_of_processes):
        process_data = []
        no_of_processes = readfile.get_num_of_processes()
        
        
        for i in range(int(no_of_processes)):
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
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)
        Priority.schedulingProcess(self, process_data)
    
    
    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key = lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''

        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                 process_data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                 process_data[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:       #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)

        Priority.printData(self, process_data, sequence_of_process)
        




    def printData(self, process_data, sequence_of_process):
        process_data.sort(key = lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("Process_ID\tArrival_Time\tRem_Burst_Time\tPriority\tCompleted\tOrig_Burst_Time\tCompletion_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t")
               
            print()

        print(f'Sequence of Process: {sequence_of_process}')


#if __name__ == "__main__":
#    no_of_processes = int(input("Enter number of processes: "))
#    priority = Priority()
#    priority.processData(no_of_processes)