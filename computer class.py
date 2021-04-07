#computer class
#class and objects concepts

class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is  :",self.cpu,self.ram)

ob1=computer("i5","12gb")
obj1=computer("ryan","79gb")

ob1.config()
obj1.config()

