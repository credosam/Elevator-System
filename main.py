from Tkinter import *
import time

allRequestButtons = []
allRequestUp = []
allRequestDown = []
allElevators = []
allFloorDoors = []
Lift1 = 1
Lift2 = 2
Lift3 = 3
Lift4 = 4

class Example(Frame):
  
	def __init__(self, parent):
		Frame.__init__(self, parent, background="grey") 
		self.parent = parent
		self.initUI()
		self.simulate()
	
	def initUI(self):
	  
		self.parent.title("Elevator System")
		self.pack(fill=BOTH, expand=1)

		leftframe = Frame(self,background = "grey",height=1000)
		label = Label(leftframe,text="Floor No",font="Helvetica 14 bold",background="grey")
		label.grid(row = 0,column=0,padx=10)

		for i in range(7):
			label = Label(leftframe, text=i+1,font = "Helvetica 14 bold",background="grey")
			label.grid(row=3*(i+1),column=0,padx=10)

		for i in range(7):
			allRequestButtons.append(RequestButton(leftframe, i+1))
			print "DONE"

		leftframe.pack(side=LEFT)
		
		#frame 1
		frame = Frame(self)
		frame.pack(side=LEFT)
		self.canvas1 = Canvas(frame, bg="grey", height=900, width=1100)

		coord1 = 10,0,10,800
		coord2 = 260,0,260,800
		coord3 = 520,0,520,800
		coord4 = 780,0,780,800
		coord5 = 1040,0,1040,800
		arc1 = self.canvas1.create_line(coord1,width=10, fill="black")
		arc2 = self.canvas1.create_line(coord2,width=10, fill="black")
		arc3 = self.canvas1.create_line(coord3,width=10, fill="black")
		arc4 = self.canvas1.create_line(coord4,width=10, fill="black")
		arc5 = self.canvas1.create_line(coord5,width=10, fill="black")

		#floordoors
		for i in range(4):
			for j in range(7):
				allFloorDoors.append(floorDoor(self.canvas1,j,i))

		#elevators
		for i in range(4):
			allElevators.append(Elevator(self.canvas1,i+1,1))

		self.canvas1.pack()

	def findNearestUp(self,destinedFloor):
		maxdiff = 10
		ele = None
		for elevator in allElevators:
			if(elevator.direction == "UP"): #and elevator.floorno > destinedFloor):
				if(abs(elevator.floorno-destinedFloor) <= maxdiff):
					maxdiff = elevator.floorno-destinedFloor
					ele = elevator
		if ele == None:
			for elevator in allElevators:
				if(elevator.direction == None):
					if(abs(elevator.floorno-destinedFloor) <= maxdiff):
						maxdiff = elevator.floorno-destinedFloor
						ele = elevator
		if ele == None:
			for elevator in allElevators:
				if(abs(elevator.floorno-destinedFloor) <= maxdiff):
					maxdiff = elevator.floorno-destinedFloor
					ele = elevator
		return ele

	def findNearestDown(self,destinedFloor):
		maxdiff = 10
		ele = None
		for elevator in allElevators:
			if(elevator.direction == "DOWN"):# and elevator.floorno < destinedFloor):
				if(abs(elevator.floorno-destinedFloor) <= maxdiff):
					maxdiff = elevator.floorno-destinedFloor
					ele = elevator
		if ele == None:
			for elevator in allElevators:
				if(elevator.direction == None):
					if(abs(elevator.floorno-destinedFloor) <= maxdiff):
						maxdiff = elevator.floorno-destinedFloor
						ele = elevator

		if ele == None:
			for elevator in allElevators:
				if(abs(elevator.floorno-destinedFloor) <= maxdiff):
					maxdiff = elevator.floorno-destinedFloor
					ele = elevator

		return ele

	def simulate(self):
		global Lift1, Lift2, Lift3, Lift4
		for request in allRequestUp:
			nearEle = self.findNearestUp(request)
			nearEle.requests.append(request)
			del allRequestUp[allRequestUp.index(request)]

		for request in allRequestDown:
			nearEle = self.findNearestDown(request)
			nearEle.requests.append(request)
			del allRequestDown[allRequestDown.index(request)]

		for elevator in allElevators:
			if len(elevator.requests) != 0:
				if elevator.y < -50+(100*elevator.requests[0]):
					elevator.update(self.canvas1,1)
					elevator.floorno = (elevator.y+50)/100
					elevator.direction = "DOWN"

				if elevator.y > -50+(100*elevator.requests[0]):
					elevator.update(self.canvas1,-1)
					elevator.floorno = (elevator.y+50)/100
					elevator.direction = "UP"

				if elevator.y == -50+(100*elevator.requests[0]):
					del elevator.requests[0]
					elevator.floorno = (elevator.y+50)/100

				# if len(elevator.requests) == 0:
				# 	elevator.direction = None

		for elevator in allElevators:
			if(elevator.elevatorNo == 1):
				Lift1 = elevator.floorno

			if(elevator.elevatorNo == 2):
				Lift2 = elevator.floorno

			if(elevator.elevatorNo == 3):
				Lift3 = elevator.floorno

			if(elevator.elevatorNo == 4):
				Lift4 = elevator.floorno
			

		for floordoor in allFloorDoors:
			floordoor.update() 

		self.parent.after(5,self.simulate)

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
		
class floorDoor(object):
	def __init__(self,w,floorNo,elevatorNo):
		self.elevatorNo = elevatorNo+1
		self.floorNo = floorNo+1
		a = -210+(260*self.elevatorNo)
		b = -50+(100*self.floorNo)
		self.window = w
		self.label = Label(self.window,text = 1,background="grey")
		self.label1 = Label(self.window, text = "Lift on floor:",background="grey")
		self.label1.place(x= a+70,y=b+20)
		self.label.place(x=a+70,y=b+40)
		self.body = self.window.create_rectangle(a,b,a+50,b+90,fill="#333333")

	def update(self):
		global Lift1, Lift2, Lift3, Lift4
		if(self.elevatorNo == 1):
			No = int(Lift1)
		elif(self.elevatorNo == 2):
			No = int(Lift2)
		elif(self.elevatorNo == 3):
			No = int(Lift3)
		else:
			No = int(Lift4)
		self.label.config(text = No)

def main():
  
	root = Tk()
	root.configure(bg = "#ffffff")

	#Setting window size
	posx = 0
	posy = 0
	screenWidth = root.winfo_screenwidth()
	screenHeight = root.winfo_screenheight()
	root.wm_geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, posx, posy))

	app = Example(root)
	root.mainloop()  


if __name__ == '__main__':
	main()  