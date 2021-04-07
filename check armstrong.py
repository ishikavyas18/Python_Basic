
# check whether it is armstrong or not


num=int(input("Enter the number to check:"))

digit=num
sum=0
while num!=0:
    temp=num%10
    sum=sum+temp**3
    num=num//10

print("Sum is :",sum)

if digit==sum:
    print("Armstrong number :",digit)
else:
    print("Not armstrong number :",digit)