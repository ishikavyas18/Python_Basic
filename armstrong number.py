

# check whether it is armstrong number or not'

num=int(input("Enter any number to check :"))

temp=num
sum=0
while num!=0:
    digit=num%10
    sum=sum+(digit**3)
    num=num//10

print("number is :",sum)

if temp==sum:
    print("Number is Armstrong ",temp)
else:
    print("Number is not Armstrong",temp)
