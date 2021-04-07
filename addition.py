
a=int(input("Enter first number :"))

b=int(input("Enter Second number :"))

sum=a+b

print("Sum of number is :"+str(sum))

# another way of printing in format
print("Sum of {0} and {1} is {2}".format(a,b,sum))

#lamba functiom

f=lambda a,b:a+b
r=f(2,3)
print(r)