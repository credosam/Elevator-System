from Tkinter import *

class floorDoor(object):
	def __init__(self,w,floorNo,elevatorNo):
		self.elevatorNo = elevatorNo+1
		self.floorNo = floorNo+1
		a = -210+(260*self.elevatorNo)
		b = -50+(100*self.floorNo)
		self.window = w
		self.label = Label(self.window,text = 0,background="grey")
		self.label1 = Label(self.window, text = "Lift on floor:",background="grey")
		self.label1.place(x= a+70,y=b+20)
		self.label.place(x=a+70,y=b+40)
		self.body = self.window.create_rectangle(a,b,a+50,b+90,fill="#333333")

	def update(self,Lift1,Lift2,Lift3,Lift4):
		if(self.elevatorNo == 1):
			No = int(Lift1)
		elif(self.elevatorNo == 2):
			No = int(Lift2)
		elif(self.elevatorNo == 3):
			No = int(Lift3)
		else:
			No = int(Lift4)
		self.label.config(text = 7-No)