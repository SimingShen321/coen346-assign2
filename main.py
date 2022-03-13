from  myscheduler import Priority




if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    priority = Priority()
    priority.processData(no_of_processes)