

# to add elements in the list we use append method

# to add all the elements of the list upto 100 which is divisible by 10

l=[]
for i in range(101):
    if i%10==0:
       l.append(i)
print(l)

print()

for x in range(0,101,10):
    l.append(x)
print(l)
