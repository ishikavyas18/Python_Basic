# to calculate avg of given number in a list

list=[1,2,3,4,55,6,66,10]

avg=0
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
print("sum is:",sum)
avg=sum/len(list)
print("average is :",avg)
