# function to count number of even and odd number from a list

list=[]
n =int(input("enter length of list :"))
for i in range(n):
    x=int(input("Enter element of list :"))
    list.append(x)
print(list)

def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd=count(list)
print(" total Even number inside the list :",even)
print("Total odd number inside the list",odd)

print("print this is format :")
print("Even : {} and Odd : {}".format(even,odd))