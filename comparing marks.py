#  operator overloading demo 2

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2


    def __gt__(self, other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        if m1>m2:
            return True
        else:
            return False

    def __str__(self):
        return '{},{}'.format(self.m1,self.m2)

s1=student(50,35)
s2=student(47,89)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")


# here we are directly printing the object so it willr return the address of the object

print(s1)

#but what if we dont want this so we have to overload __str__
print(s2)