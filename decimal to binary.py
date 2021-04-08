

# convert decimal to binary using recursion
from math import *
number=int(input("Enter the decimal number :"))

binary=0
while number>0:
    temp=number%2
    binary=binary*10+temp
    number=number//2

print("binary is",binary)

print("cross check :",bin(number))


print("using recusrsion ::")

def bi(number):
    if number>1:
        bi(number//2)
    print(number%2,end='')
dec=34
bi(dec)

