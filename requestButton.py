from Tkinter import *

allRequestUp = []
allRequestDown = []

class RequestButton(object):
	def __init__(self, w, floorNo):
		self.floorNo = floorNo
		self.window = w
		self.rButton1 = Button(self.window, text="UP", command=self.createRequestUp)
		self.rButton2 = Button(self.window, text="DN", command=self.createRequestDown)
		self.rButton1.grid(column=2,row=3*floorNo+1,padx=50)
		self.rButton2.grid(column=2,row=3*floorNo+2,pady=6)
		
	def createRequestUp(self):
		allRequestUp.append(self.floorNo)

	def createRequestDown(self):
		allRequestDown.append(self.floorNo)