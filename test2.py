class Process(list):
	def __init__(self):
		self = []

	def add(self,name,arrival, burst):
		self.append({'name':name,'arrival':arrival,'burst':burst})
	def show(self):
		for i in self:
			print(i)
	def resultset(self,index,ans):
		c=ans[0]
		t=ans[1]
		w=ans[2]
		self[index]={'completion':c,'turnaround':t,'waiting':w}


plist = Process()
plist.add(0,1,2)
print(plist)
plist.resultset(0,[3,4,5])
print(plist)