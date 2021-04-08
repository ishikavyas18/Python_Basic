#create an array with 5 element and delete the value at index 2 without built in function

from array import *

arr=array('i',[])
n=int(input("enter length :"))
for i in range(n):
    x=int(input("enter next element :"))
    arr.append(x)
print("array is  :",arr)
arr1=array('i',[])

del_element=int(input("enter elemnet to be deleted : "))

for element in arr:
    if element==del_element:
        continue
    else:
         arr1.append(element)
print(arr1)