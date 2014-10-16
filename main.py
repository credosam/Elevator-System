from Tkinter import *
import time

allRequestButtons = []
allRequestUp = []
allRequestDown = []
allElevators = []
allFloorDoors = []
Lift1 = "1"
Lift2 = "2"
Lift3 = "3"
Lift4 = "4"

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="grey")    
        self.parent = parent
        self.initUI()
    
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

        coord1 = 10,0,10,800
        coord2 = 260,0,260,800
        coord3 = 520,0,520,800
        coord4 = 780,0,780,800
        coord5 = 1040,0,1040,800
        frame = Frame(self)
        frame.pack(side=LEFT)

        canvas1 = Canvas(frame, bg="grey", height=900, width=1100)
        arc1 = canvas1.create_line(coord1,width=10, fill="black")
        arc2 = canvas1.create_line(coord2,width=10, fill="black")
        arc3 = canvas1.create_line(coord3,width=10, fill="black")
        arc4 = canvas1.create_line(coord4,width=10, fill="black")
        arc5 = canvas1.create_line(coord5,width=10, fill="black")

        #Lifts
        for i in range(4):
        	for j in range(7):
        		allFloorDoors.append(floorDoor(canvas1,j,i))
        		

        canvas1.pack()

        

class RequestButton(object):
    def __init__(self, w, floorNo):
        self.floorNo = floorNo
        self.window = w
        self.rButton1 = Button(self.window, text="UP", command=self.createRequestUp(floorNo))
        self.rButton2 = Button(self.window, text="DN", command=self.createRequestDown(floorNo))
        label = Label(self.window,text="DDD")
        self.rButton1.grid(column=2,row=3*floorNo+1,padx=50)
        self.rButton2.grid(column=2,row=3*floorNo+2,pady=6)
        
    def createRequestUp(self,floorNo):
        allRequestUp.append(floorNo)

    def createRequestDown(self,floorNo):
    	allRequestDown.append(floorNo)

class Elevator(object):
    def __init__(self, w, No):
        self.elevatorNo = No
        self.window = w
        self.opened = False
        

class floorDoor(object):
	def __init__(self,w,floorNo,elevatorNo):
		a = -210
		b = -50
		c = -160
		d = 40
		self.elevatorNo = elevatorNo+1
		self.floorNo = floorNo+1
		self.window = w
		if self.elevatorNo == 1:
			No = Lift1
		elif self.elevatorNo == 2:
			No = Lift2
		elif self.elevatorNo == 3:
			No = Lift3
		else:
			No = Lift4
		self.label = Label(self.window,text = No,background="grey")
		self.label1 = Label(self.window, text = "Lift on floor:",background="grey")
		self.label1.place(x= c+20+self.elevatorNo*260,y=b+20+(100*self.floorNo))
		self.label.place(x=c+20+self.elevatorNo*260,y=b+40+(100*self.floorNo))
		self.body = self.window.create_rectangle(a+(260*self.elevatorNo),b+(100*self.floorNo),c+(260*self.elevatorNo),d+(100*self.floorNo),fill="#333333")



# def simulate()

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


