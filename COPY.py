#copying of two array
from array import *

arr=array('i',[1,2,3,4])

arr2=array('i',[])

arr2=arr
#for i in arr2:

print(arr2)
print(id(arr))
print(id(arr2))