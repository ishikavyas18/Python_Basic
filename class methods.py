# class method demo

class student:
    school='IIPS'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):   # instance methods because they are accessing with objects
        return ((self.m1+self.m2+self.m3)/3)

    #class method (self keyword instance method mei aata hai class methods class variab;e ki value change krne ke liye hota hai or cls keyword lgate hai)

    @classmethod
    def info(cls):
        return(cls.school)

    @staticmethod
    def information():
        print("this is static method and it has nothing to do with class method and object")

s1=student(23,12,14)
s2=student(10,10,10)
print(student.info())
#print(student.info(s2))
#print(s2.info())
student.information()


print(s1.avg())
print(s2.avg())