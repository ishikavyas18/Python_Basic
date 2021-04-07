#code for adding two array using for loop


from array import *

arr=array('i',[])
m=int(input("Enter length of array 1: "))
for i in range(m):
    x=int(input("Enter elements in array 1:"))
    arr.append(x)
print("first array is :",arr)
arr1=array('i',[])
n=int(input("Enter legth of second array:"))
for j in range(n):
    y=int(input("enter elements in second array :"))
    arr1.append(y)
print("second array :",arr1)

c=array('i',[])
for j in range(n):
    c.append(arr[i]+arr1[j])
print(c)

