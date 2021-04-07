class Vehicle:
    def __init__(self,registration_number):
        self.registration_number=registration_number
    def run(self):
        print("Vehicle is running")
    def start(self):
        print("vehicle is started")
    def stop(self):
        print("vehicle is stopped")

class fourwheeler(Vehicle):
    def run(self):
        print("the four wheeler is running")
        super().run()
    def stop(self):
        print("the four wheeler stopped")

class car(fourwheeler):
    def __init__(self,registration_number,is_commercial):
        super().__init__(registration_number)
        self.is_commercial=is_commercial
    def run(self):
        print("the car is running")
        super().run()
    def start(self):
        print("the car stared")
        super().run()
        super().stop()

car=car(8585,False)
car.start()