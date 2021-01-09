from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random

class App:
	def __init__(self,root):
		self.root = root
		self.root.title("CPU Scheduling Calculator")
		# self.root.geometry("600x500")

		self.algorithms = ["fcfs",'sjf','srtf',] # choices of algorithms
		self.nProcess = IntVar(value=3) #default number of process
		self.processes=[] #where processes will be stored
		
		for i in range(self.nProcess.get()):
			self.processes.append([ IntVar() for i in range(3)])
			

		''' TOP MENU '''
		#algorithm dropdown
		self.topFrame=Frame(self.root)
		# Label(self.topFrame, text='	').pack(side=TOP)
		self.algoLabel= Label(self.topFrame,text="Choose Algorithm",font='Helvetica 12 bold').pack(side=LEFT,expand=True,fill='x')
		self.algochoice=StringVar(value=self.algorithms[0])
		self.algomenu = OptionMenu(self.topFrame,self.algochoice,*self.algorithms)
		self.algomenu.pack(side=LEFT)
		self.algomenu.config(font='Helvetica 12 bold',bg='white')
		self.algomenu['menu'].config(font='Helvetica 12 bold',bg='white')
		#increase and decrease button
		Label(self.topFrame, text='	').pack(side=LEFT)
		self.deccButton = Button(self.topFrame,text='-',command=self.decreaseProcess,font='Helvetica 12 bold').pack(side=LEFT,expand=True,fill='x')
		self.nProcessLabel = Label(self.topFrame, textvariable=self.nProcess,font='Helvetica 12 bold').pack(side=LEFT,expand=True,fill='x')
		self.incButton = Button(self.topFrame,text='+',command=self.inreaseProcess,font='Helvetica 12 bold').pack(side=LEFT,expand=True,fill='x')
		Label(self.topFrame, text='	').pack(side=LEFT)
		
		''' MID TABLE '''
		self.tableFrame=Frame(self.root)
		self.labels=['process','arrival','burst','priority','completion','turnaround','waiting'] #list of time labels
		for i,label in enumerate(self.labels):
			Label(self.tableFrame, text=label,bg='white',relief='raised',width=9,font='12').grid(row=1,column=i) #printing time labels above the table

		self.table=[]
		for i,process in enumerate(self.processes): #displaying table
			row=i+2
			label=Label(self.tableFrame,text='P'+str(i+1),width=9,relief=FLAT,bg='white',font='12',bd=2) #printing process's names
			label.grid(row=row,column=0)
			row_table=[label]
			for i,data in enumerate(process):
				entry=Entry(self.tableFrame,textvariable=data,width=9,relief=FLAT,bg='white',font='12',bd=2,justify=CENTER) #printing entry fields for inputs (arrival, burst and priority)
				entry.grid(row=row,column=i+1)
				row_table.append(entry)
			self.table.append(row_table)

		self.chartFrame=Frame(self.root)
		self.ganttchart()

		self.topFrame.pack(expand=True,fill='both')
		self.tableFrame.pack()
		self.chartFrame.pack()
		


	def decreaseProcess(self):
		if self.nProcess.get() > 1:
			self.nProcess.set(self.nProcess.get()-1)
			for cell in self.table[-1]:
				cell.grid_forget()	
			self.table.pop()
			self.processes.pop()
						
	def inreaseProcess(self):
		nProcess=self.nProcess.get() 
		if nProcess < 10:
			self.nProcess.set(nProcess+1)
			self.processes.append([ IntVar() for i in range(3)]) #actual data variable
			row=nProcess+2
			label=Label(self.tableFrame,text='P'+str(nProcess+1),width=9,relief=FLAT,bg='white',font='12',bd=2) #adding widget
			label.grid(row=row,column=0)
			row_table=[label] 
			for i,data in enumerate(self.processes[-1]):
				entry=Entry(self.tableFrame,textvariable=data,width=9,relief=FLAT,bg='white',font='12',bd=2,justify=CENTER) #printing entry fields for inputs (arrival, burst and priority)
				entry.grid(row=row,column=i+1)
				row_table.append(entry)
			self.table.append(row_table)
			print(self.nProcess.get())
		
	def ganttchart(self):
		fig = plt.Figure(figsize=(6,0.9)
			, tight_layout=True
			)
		ax = fig.add_subplot(111)
		labels=(1,2,3)
		ax.broken_barh([(0, 3), (3, 2), (5, 5)], (0, 1),
		               facecolors=('tab:orange', 'tab:green', 'tab:red'),label=labels)
		

		ax.text(1.5,0.4,"test",
			horizontalalignment='center',
			verticalalignment='center',
			fontsize=12)

		ax.set_xlim(0, 10)
		ax.set_ylim(0, 1)
		ax.set_xticks(np.arange(0,11))
		ax.set_yticks([])
		ax.set_xlabel('milliseconds')
		# ax.grid(True)
		fig.set()
		# plt.show()
		canvas = FigureCanvasTkAgg(fig, master=self.chartFrame)
		canvas.draw()
		canvas.get_tk_widget().pack(side=BOTTOM)



def main():
	root = Tk()
	app = App(root)

	app.root.mainloop()

if __name__ == "__main__":
	main()