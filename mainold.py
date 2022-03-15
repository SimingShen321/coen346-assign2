from  myscheduler import Priority
import readfile


if __name__ == "__main__":
    no_of_processes = readfile.get_num_of_processes()
    priority = Priority()
    priority.processData(no_of_processes)
    