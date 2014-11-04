from Tkinter import *

class Elevator(object):
	def __init__(self, w, ele,flr):
		self.elevatorNo = ele
		self.window = w
		self.direction = None
		self.opened = False
		self.floorno = flr
		self.requests = []
		self.x = -210+(260*self.elevatorNo)
		self.y = -50+(100*self.floorno)
		self.body = self.window.create_rectangle(self.x,self.y,self.x+50,self.y+90, fill="red")

	def update(self,w,vel):
		self.vel = vel
		self.window = w
		self.window.move(self.body,0, self.vel)
		self.x = self.window.coords(self.body)[0]
		self.y = self.window.coords(self.body)[1]
		self.window.update()