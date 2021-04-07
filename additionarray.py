# addition of two array

from array import *

arr=array('i',[1,2,3])
arr1=array('i',[1,2,3])
arr2=array('i',[])
sum=0
for i in range(len(arr)):
    for j in range(len(arr1)):

        arr2.append(arr[i]+arr1[j])
    print(arr2)