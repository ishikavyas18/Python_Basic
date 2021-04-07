
# program to count number of digits

n=int(input("Enter the number :"))

count=0

while n!=0:
    temp=n%10
    n=n//10
    count+=1
print(count)
