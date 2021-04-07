# educative task 3

# car and engine object and class relationship

class car:
    def __init__(self,model,color):
        self.model =model
        self.color = color


    def printDetails(self):


        print("model is :", self.model)
        print("color is :", self.color)

    pass
class sedanengine:
    def start(self):
        print("car is started")
    pass
    def stop(self):
        print("car stopped")

class sedan(car):
    def __init__(self,model,color):
        super().__init__(model,color)
        self.engine=sedanengine()
    def setStart(self):
        self.engine.start()
    def setStop(self):
        self.engine.stop()
car1=sedan("toyota","grey")
car1.setStart()
car1.printDetails()
car1.setStop()
