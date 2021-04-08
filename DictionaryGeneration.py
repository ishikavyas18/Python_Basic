
# program to generate dictionary that contains number between 1 to n in form of(x,x**X)

num=int(input("enter the number:"))
d={x:x*x for x in range(1,num+1)}
print(d)