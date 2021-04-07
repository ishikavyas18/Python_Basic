
# armstrong number in certain interval
lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
for i in range(lower,upper+1):
    num=i
    sum=0
    # to find out digits present in a number
    n=len(str(i))
    while i!=0:
        reverse=i%10
        sum=sum+reverse**n
        i=i//10

    #print("sum is: ",sum)
    if num==sum:
        print("Armstrong number :",num)

