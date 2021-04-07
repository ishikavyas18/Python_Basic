
# check whether armstrong or not
num=int(input("Enter number: "))
sum=0
s=num
temp=num
#n=len(num)
count=0
while num!=0:

    count=count+1
    num=num//10
#print(count)
print("Total number of digit is :",count)
while temp!=0:
    rev=temp%10

    sum=sum+rev**count
    temp=temp//10
print("Number is :",sum)
#print(temp)
#print(s)

if sum==s:
    print("Number is armstrong")
else:
    print("number is not armstrong")
