from Tkinter import *
allRequestEle1 = []
allRequestEle2 = []
allRequestEle3 = []
allRequestEle4 = []
elevatorStop1 = False
elevatorStop2 = False
elevatorStop3 = False
elevatorStop4 = False

class ElevatorButtons(object):
	def __init__(self,w,elevatorNo):
		self.elevatorNo = elevatorNo
		self.window = w
		self.makeButtons()

	def makeButtons(self):
		self.Button0 = Button(self.window, text="0", command=lambda: self.createRequestEle(7))
		self.Button0.place(x=-210+(260*self.elevatorNo),y=5)

		self.Button1 = Button(self.window, text="1", command=lambda: self.createRequestEle(6))
		self.Button1.place(x=-170+(260*self.elevatorNo),y=5)

		self.Button2 = Button(self.window, text="2", command=lambda: self.createRequestEle(5))
		self.Button2.place(x=-130+(260*self.elevatorNo),y=5)

		self.Button3 = Button(self.window, text="3", command=lambda: self.createRequestEle(4))
		self.Button3.place(x=-90+(260*self.elevatorNo),y=5)

		self.Button4 = Button(self.window, text="4", command=lambda: self.createRequestEle(3))
		self.Button4.place(x=-50+(260*self.elevatorNo),y=5)

		self.Button5 = Button(self.window, text="5", command=lambda: self.createRequestEle(2))
		self.Button5.place(x=-130+(260*self.elevatorNo),y=40)

		self.Button6 = Button(self.window, text="6", command=lambda: self.createRequestEle(1))
		self.Button6.place(x=-90+(260*self.elevatorNo),y=40)

		self.stopButton = Button(self.window, text="||", command=lambda: self.stopRequestEle())
		self.stopButton.place(x=-50+(260*self.elevatorNo),y=40)

	def createRequestEle(self,requestedFloor):
		if self.elevatorNo == 1:
			allRequestEle1.append(requestedFloor)
		elif self.elevatorNo == 2:
			allRequestEle2.append(requestedFloor)
		elif self.elevatorNo == 3:
			allRequestEle3.append(requestedFloor)
		else:
			allRequestEle4.append(requestedFloor)

	def stopRequestEle(self):
		global elevatorStop1,elevatorStop2,elevatorStop3,elevatorStop4
		if self.elevatorNo == 1:
			elevatorStop1 = True
		elif self.elevatorNo == 2:
			elevatorStop2 = True
		elif self.elevatorNo == 3:
			elevatorStop3 = True
		else:
			elevatorStop4 = True