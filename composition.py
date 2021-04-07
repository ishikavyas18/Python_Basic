# demo of compostition
# a car class is the owner class class which has object of its owned class i.e engine , door , tier

class engine:
    def __init__(self,capacity):
        self.capacity=capacity
    def printDetails(self):
        print("Engine Details :",self.capacity)

class tier:
    def __init__(self,tier=0):
        self.tier=tier
    def printDetails(self):
        print("Total number of tier is :",self.tier)

class door:
    def __init__(self,door):
        self.door=door
    def printDetails(self):
        print("Total doors are :",self.door)

class car:
    def __init__(self,eng,tr,dr,color):
        self.eobj=engine(eng)
        self.tobj=tier(tr)
        self.dobj=door(dr)
        self.color=color

    def printDetails(self):
        self.eobj.printDetails()
        self.tobj.printDetails()
        self.dobj.printDetails()
        print("color is :",self.color)

c=car("fg",4,4,"fhjf")
c.printDetails()