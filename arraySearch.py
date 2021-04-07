#taking the value of array from the user and search for the particular value :

from array import *

arr=array('i',[]) # creating a blank array
n=int(input("enter length of array :"))
for i in range(n):
    x=int(input("enter next value :"))
    arr.append(x)
print(arr)

val=int(input("enter the element to be search :"))
k=0 # for index
for e in arr:
    if e==val:
        print(k)
        #print(arr.index(e))

        break
    k+=1

#search using built in function
#print(arr.index(val))