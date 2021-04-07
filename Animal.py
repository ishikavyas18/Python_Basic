
# educative task 2

# animal class polymorphism

class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

    def animalDetails(self):
        print("name of animal :",self.name)
        print("sound of animal :",self.sound)

class dog(animal):
    def __init__(self,name,sound,family):
        super().__init__(name,sound)
        self.family=family
    def animalDetails(self):
        super().animalDetails()
        print("family is :",self.family)
class sheep(animal):
    def __init__(self,name,sound,color):
        super().__init__(name,sound)
        self.color=color
    def animalDetails(self):
        super().animalDetails()
        print("Color is :",self.color)
d=dog("pongo","who who","husky")
d.animalDetails()
print("")
s=sheep("billy","baa baa","white")
s.animalDetails()