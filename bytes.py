# demo of bytes datatype and bytearray
#byte and byte array both are same only difference is that byte arrray is mutable where as byte is not

x=[10,20,30,40]

b=bytes(x)

print(b[0])
print("values of byte is as follows :")
for i in b:
    print(i)

c=bytearray(x)

print("Acessing element using index :",c[0])
print("values of byte array is: ")
for a in c:
    print(a)

c[0]=90
print("bytes array is mutable",c[0])
print("after changing value of byte array :")
for z in c:
    print(z)

d={}
print(type (d))

s=set()
print(type(s))



