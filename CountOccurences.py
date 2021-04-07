
list=list(map(int,input().split(",")))

x=int(input("Enter element to count occurence :"))

count=0
for i in range(0,len(list)):
    if x==list[i]:
        count=count+1
if count!=0:
    print(count)
else:
    print(-1)
