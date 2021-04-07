

# program to create simple calculator

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a//b

#print("Enter choice : 1 for addition ,end='' 2 for subtraction , end='', 3 for multiplication ,end='', 4 for division")
print("Select Operation :")
print(" 1 for addition")
print(" 2 for subtraction")
print(" 3 for multiplication")
print(" 4 for division")
choice=int(input("Enter choice :"))
if choice==1:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print("Addition is :",add(num1,num2))
elif  choice==2:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print("Subtraction is :",subtract(num1,num2))
elif choice==3:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print("Multiplication is :",multiply(num1,num2))
elif choice==4:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print("Divison is :",division(num1,num2))
else:
    print("Renter choice")


