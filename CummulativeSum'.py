
# to find the cummulative sum of given number

list=[10,20,30,40,50]
sum=0
clist=[]
for i in range(len(list)):
    sum=sum+list[i]
    #print(sum)
    clist.append(sum)
print(clist)