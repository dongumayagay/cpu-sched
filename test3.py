processes={
'P0':{'arrival':0, 'burst':7, 'completion':0,'turnaround':0,'waiting':0},
'P1':{'arrival':2, 'burst':4, 'completion':0,'turnaround':0,'waiting':0},
'P2':{'arrival':4, 'burst':1, 'completion':0,'turnaround':0,'waiting':0},
'P3':{'arrival':13, 'burst':4, 'completion':0,'turnaround':0,'waiting':0},
}

for i in processes:
	print(i)
# print(processes[0].keys())
print()
print(processes['P0'])

processes = sorted(processes, key = lambda x:x[0]['arrival'])