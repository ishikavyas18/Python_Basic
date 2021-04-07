

#conditional statement

a=int(input("Enter first Number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if a>b and a>c:
    print("%d is bigger among all "&a)
elif b>a and b>c:
    print("%d is bigger among all"%b)
else:
    print("%d is bigger among all" %c)

# to check whether the number is in range of 1 to 100

n=int(input("Enter the number :"))
if n>=1 and n<=100:
    print("%d is in range" %n)
else:
    print("not in range")