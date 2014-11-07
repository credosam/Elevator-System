from Tkinter import *
from time import *

class Elevator(object):
	def __init__(self, w, ele,flr):
		self.elevatorNo = ele
		self.window = w
		self.direction = None
		self.open = False
		self.count = 0
		self.stop = False
		self.floorno = flr
		self.requests = []
		self.x = -210+(260*self.elevatorNo)
		self.y = -50+(100*self.floorno)
		self.body = self.window.create_rectangle(self.x,self.y,self.x+50,self.y+90, fill="red")
		self.body1 = self.window.create_rectangle(self.x,self.y,self.x,self.y+90, fill="white")
		self.body2 = self.window.create_rectangle(self.x+50,self.y,self.x+50,self.y+90, fill="white")

	def update(self,w,vel):
		self.vel = vel
		self.window = w
		self.window.move(self.body,0, self.vel)
		self.x = self.window.coords(self.body)[0]
		self.y = self.window.coords(self.body)[1]
		self.window.update()

	def gateOpen(self,count):
		self.window.coords(self.body1,self.x+25-count,self.y,self.x+25,self.y+90)
		self.window.coords(self.body2,self.x+25,self.y,self.x+25+count,self.y+90)
		# self.window.itemconfig(self.body1,bbox=(self.x,self.y,self.x+count,self.y+90))
		# self.window.itemconfig(self.body2,coords=(self.x+50-count,self.y,self.x+50,self.y+90))
		# self.window.update()

	def gateClose(self,count):
		self.window.coords(self.body1,self.x+count,self.y,self.x+25,self.y+90)
		self.window.coords(self.body2,self.x+25,self.y,self.x+50-count,self.y+90)
		# self.window.itemconfig(self.body1,coords=(self.x,self.y,self.x+25-count,self.y+90))
		# self.window.itemconfig(self.body2,coords=(self.x+25+count,self.y,self.x+50,self.y+90))
		# self.window.update()
