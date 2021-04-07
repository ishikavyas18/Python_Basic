
#armstrong number concept

num=int(input("Enter number:"))
temp=num
check=num
sum=0
count=0
#l=len(str(num))
#print(l)
while num!=0:
    count=count+1

#print(count)
while temp!=0:
    r=temp%10
    sum=sum+(r**count)
    temp=temp//10
print("Sum is:",sum)
if sum==check:
    print("Armstrong Number")
else:
    print("Not an armstrong number")