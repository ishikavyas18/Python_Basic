#comparing two objects

class computer:
    def __init__(self,name,age):
        self.name='navin'
        self.age=78


    def compare(self,obj):
        if self.age==obj.age:
            return  True
        else:
            return False
ob=computer('navin',89)
ob.age=90
obj=computer('rashi',87)

if ob.compare(obj):
    print("they are equal")
else:
    print("they are not same")

print(ob.name)
print(obj.name)