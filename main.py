from Tkinter import *
import time
from elevatorButton import *
from requestButton import *
from elevator import *
from floorDoors import *

allRequestButtons = []
allElevators = []
allFloorDoors = []
allElevatorButtons = []
# allRequestEle = [[]]
# allRequestEle.append(allRequestEle4)
# allRequestEle.append(allRequestEle3)
# allRequestEle.append(allRequestEle2)
# allRequestEle.append(allRequestEle1)

Lift1 = 0
Lift2 = 0
Lift3 = 0
Lift4 = 0

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
			label = Label(leftframe, text=6-i,font = "Helvetica 14 bold",background="grey")
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
			allElevators.append(Elevator(self.canvas1,i+1,7))

		for i in range(4):
			allElevatorButtons.append(ElevatorButtons(self.canvas1,i+1))

		self.canvas1.pack()

	def findNearestUp(self,destinedFloor):
		maxdiff = 10
		ele = None
		for elevator in allElevators:
			if(elevator.direction == "UP"and elevator.floorno > destinedFloor):
				if(abs(elevator.floorno-destinedFloor) < maxdiff):
					maxdiff = elevator.floorno-destinedFloor
					ele = elevator
		if ele == None:
			for elevator in allElevators:
				if(elevator.direction == None):
					if(abs(elevator.floorno-destinedFloor) < maxdiff):
						maxdiff = elevator.floorno-destinedFloor
						ele = elevator
		# if ele == None:
		# 	for elevator in allElevators:
		# 		if(abs(elevator.floorno-destinedFloor) < maxdiff):
		# 			maxdiff = elevator.floorno-destinedFloor
		# 			ele = elevator
		return ele

	def findNearestDown(self,destinedFloor):
		maxdiff = 10
		ele = None
		for elevator in allElevators:
			if(elevator.direction == "DOWN" and elevator.floorno < destinedFloor):
				if(abs(elevator.floorno-destinedFloor) < maxdiff):
					maxdiff = elevator.floorno-destinedFloor
					ele = elevator
		if ele == None:
			for elevator in allElevators:
				if(elevator.direction == None):
					if(abs(elevator.floorno-destinedFloor) < maxdiff):
						maxdiff = elevator.floorno-destinedFloor
						ele = elevator

		# if ele == None:
		# 	for elevator in allElevators:
		# 		if(abs(elevator.floorno-destinedFloor) < maxdiff):
		# 			maxdiff = elevator.floorno-destinedFloor
		# 			ele = elevator

		return ele

	def simulate(self):
		global Lift1, Lift2, Lift3, Lift4
		for request in allRequestUp:
			nearEle = self.findNearestUp(request)
			if nearEle is not None:
				nearEle.direction = "UP"
				nearEle.requests.append(request)
				del allRequestUp[allRequestUp.index(request)]

		for request in allRequestDown:
			nearEle = self.findNearestDown(request)
			if nearEle is not None:
				nearEle.direction = "DOWN"
				nearEle.requests.append(request)
				del allRequestDown[allRequestDown.index(request)]

		for elevator in allElevators:
			if elevator.direction == "UP":
				elevator.requests.sort(reverse=True)
			elif elevator.direction == "DOWN":
				elevator.requests.sort()

		# for elevator in allElevators:
		# 	if len(elevator.requests) != 0:
		# 		print "allright"
		# 		print elevator.elevatorNo
		# 		print elevator.requests

		for elevator in allElevators:
			if len(elevator.requests) != 0:
				if elevator.y < -50+(100*elevator.requests[0]):
					elevator.update(self.canvas1,1)
					elevator.floorno = (elevator.y+50)/100
					# elevator.direction = "DOWN"

				if elevator.y > -50+(100*elevator.requests[0]):
					elevator.update(self.canvas1,-1)
					elevator.floorno = (elevator.y+50)/100
					# elevator.direction = "UP"

				if elevator.y == -50+(100*elevator.requests[0]):
					del elevator.requests[0]
					elevator.floorno = (elevator.y+50)/100
					elevator.open = True
					elevator.count = 0
					# elevator.gateOpen()

			if elevator.open == True:
				if elevator.count < 26:
					elevator.gateOpen(elevator.count)
					sleep(0.01)
					elevator.count = elevator.count + 1
				elif elevator.count >= 26 and elevator.count <51:
					elevator.gateClose(elevator.count-25)
					sleep(0.01)
					elevator.count = elevator.count + 1
				else:
					elevator.open = False
					elevator.count = 0

			if elevator.open == True:
				if(elevator.elevatorNo == 1):
					elevator.requests.extend(allRequestEle1)

				if(elevator.elevatorNo == 2):
					elevator.requests.extend(allRequestEle2)

				if(elevator.elevatorNo == 3):
					elevator.requests.extend(allRequestEle3)

				if(elevator.elevatorNo == 4):
					elevator.requests.extend(allRequestEle4)

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
			floordoor.update(Lift1,Lift2,Lift3,Lift4) 

		self.parent.after(5,self.simulate)

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