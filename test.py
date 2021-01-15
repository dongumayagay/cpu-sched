# processes=[
# {'name':0,'arrival':0, 'burst':7, 'completion':0,'turnaround':0,'waiting':0},
# {'name':1,'arrival':2, 'burst':4, 'completion':0,'turnaround':0,'waiting':0},
# {'name':2,'arrival':4, 'burst':1, 'completion':0,'turnaround':0,'waiting':0},
# {'name':3,'arrival':13, 'burst':4, 'completion':0,'turnaround':0,'waiting':0},
# ]
import copy
processes=[
{'name':0,'arrival':1, 'burst':5, 'priority':0, 'completion':0,'turnaround':0,'waiting':0, 'bar':[]},
{'name':1,'arrival':2, 'burst':3, 'priority':0, 'completion':0,'turnaround':0,'waiting':0, 'bar':[]},
{'name':2,'arrival':2, 'burst':4, 'priority':0, 'completion':0,'turnaround':0,'waiting':0, 'bar':[]},
]

queue=processes.copy()
def fcfs():

	queue = sorted(processes, key = lambda x:x['arrival'])
	timecounter=0

	while len(queue) != 0: #check if there is still process in the queue
		process = queue[0] #since this is already sorted by arrival just check if the first process reamining is waiting
		if process['arrival'] <= timecounter: # if it is waiting process it and since it is non preemptive just wait theprocess to fully complete
			process_index=processes.index(process)
			processes[process_index]['bar'].append((timecounter,process['burst'])) # for gantt chart
			timecounter+=process['burst'] #add the burst time because this mean that is the process is already finish
			processes[process_index]['completion'] = timecounter # completion time
			queue.remove(process) #after completion remove it to the list of process
		else: #if there is no process going on
			timecounter+=(process['arrival']-timecounter) #check the difference of time now and next process' arrival time
	print(timecounter)
	print(len(queue))

def sjf():
	queue = sorted(processes, key = lambda x:x['burst']) #first short by burst time then sort by arivval
	queue.sort(key = lambda x:x['arrival'])
	timecounter = 0
	while len(queue) != 0: #check if there is still process in the queue
		process = queue[0] #since this is already sorted by arrival and burst just check the first process in the queue
		if process['arrival'] <= timecounter: # if it is waiting process it and since it is non preemptive just wait theprocess to fully complete
			process_index=processes.index(process)
			processes[process_index]['bar'].append((timecounter,process['burst'])) # for gantt chart
			timecounter+=process['burst'] #add the burst time because this mean that is the process is already finish
			processes[process_index]['completion'] = timecounter # completion time
			queue.remove(process) #after completion remove it to the list of process
		else: #if there is no process going on
			timecounter+=(process['arrival']-timecounter) #check the difference of time now and next process' arrival time
	print(timecounter)

def srtf(queue):
	queue = queue
	# queue = sorted(processes, key = lambda x:x['burst'])
	# queue = copy.deepcopy(processes)

	# queue = queue
	timecounter = 0
	while len(queue) != 0: #check if there is still process in the queue
		queue.sort(key = lambda x:x['burst'])
		queue.sort(key = lambda x:x['arrival'])
		process = queue[0] #since this is already sorted by arrival and burst just check the first process in the queue
		if process['arrival'] <= timecounter: # if it is waiting process it and since it is non preemptive just wait theprocess to fully complete
			process['burst'] -= 1
			process_index=processes.index(process)
			if process['burst'] == 0:
				queue.remove(process)

		timecounter += 1
	print(len(queue))
			
	print(timecounter)
# fcfs()
srtf(queue)
for i in processes:
	print(i)