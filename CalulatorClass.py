# educative task 3

# calculator class

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return (self.num1+self.num2)
    def subtract(self):
        return (self.num2-self.num1)
    def multiply(self):
        return (self.num1*self.num2)
    def divide(self):
        return (self.num2/self.num1)
ob=Calculator(10,20)
print(ob.add())
print(ob.subtract())
print(ob.multiply())
print(ob.divide())