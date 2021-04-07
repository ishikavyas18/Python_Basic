

# find armstrong number in an interval

lower=int(input("Enter lower bound :"))

upper=int(input("Enter lower bound :"))
#sum=0
for num in range(lower,upper+1):
    sum=0
    count=0
    digit =num
    #print(num)
    while num!=0:
        temp=num%10
        sum=sum+temp**3
        num=num//10
    print("sum is :",sum)
    if digit==sum:
        print("armstrong found",digit)
        count+=1
        break
    else:
        print("Not Found",digit)
print("Total count is :",count)

