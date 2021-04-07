# array demo and its method

from array import *

vals=array('i',[1,23,45,6,7,8,-1])

print("printing values of array :")
print(vals)

print("-----------------------------------------------------------------------------------------------------------------")

print("sixe of array is  :",vals.buffer_info())

print("typecode of array is :",vals.typecode)
vals.append(22)
print("array after adding element :",vals)

print("to insert element at particular index")

vals.insert(2,100)
print(vals)

print("removing element from an array :")
vals.remove(100)
print(vals)

print("now reverse of an array :")
vals.reverse()
print(vals)

print("removing last elemnet from array :")
vals.pop()
print(vals)

print("again reverse array to see index accessing:")
vals.reverse()
print(vals)

print("value at a particular index :",vals[0])

print("-----------------------------------------------------------------------------------------------------------------")
#method 1
#for i in range(7):
 #   print("value are :",vals[i])


#method 2

#for i in range(len(vals)):
  #  print(vals[i])

#method 3

for i in vals:
    print(i)


print("to create a new array with same elements as vals")

newarr=array(vals.typecode,(a for  a in vals))

print("copied array is :",newarr)

print("instead of printing same array as old one what if we print square of old array :")

newar=array(vals.typecode,(j*j for j in vals))
#print("squared elements are :",newar)
for a in newar:

  print(a)

print("printing using while loop :")

i=0
while i<len(vals):
    print(vals[i])
    i=i+1