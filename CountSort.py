

arr=[1,4,1,2,7,5,2]
n=len(arr)

m=max(arr)+1
#print(m)
#creating count array and initalise it with 0
count=[0]*m
#print("gh",count)
for i in range(len(arr)):
    count[arr[i]]+=1
#print(count)
# adding previous element to the last

for j in range(1,len(count)):
    count[j]=count[j]+count[j-1]
#print(count)

# create another array as output array of same size as input array
arr2=[0]*len(arr)
for j in range(n-1,-1,-1):
    arr2[count[arr[j]]-1]=arr[j]
    count[arr[j]]=count[arr[j]]-1
print(*arr2)