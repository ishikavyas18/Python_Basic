# add certain number to each and every element in an array


from array import *

arr=array('i',[1,2,3,4,5])
#arr1=array('i',[1,2,3,4,5])
print(arr)
#print(arr1)

for i in range(len(arr)):
    arr[i]=arr[i]+5
print("after adding",arr)
