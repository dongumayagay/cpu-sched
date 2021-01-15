processes=[
{'name':0,'arrival':0, 'burst':7, 'completion':0,'turnaround':0,'waiting':0},
{'name':1,'arrival':2, 'burst':4, 'completion':0,'turnaround':0,'waiting':0},
{'name':2,'arrival':4, 'burst':1, 'completion':0,'turnaround':0,'waiting':0},
{'name':3,'arrival':0, 'burst':4, 'completion':0,'turnaround':0,'waiting':0},
]

# processes.sort(key = lambda x : x['arrival'])
counter = 0
q = [ process for process in processes if process['arrival'] <= counter]

for i in q:
	print(i)

print()

q.sort(key = lambda x : x['burst'])

for i in q:
	print(i)

c = q[0]

print()

print(c)

processes.remove(c)

print()

for i in processes:
	print(i)