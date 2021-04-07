


# wap to print all character of strring along with positive and negative index

s=input("Enter String  :")

i=0
for x in s:
    print("The character at positive index {} and at negative index {} is {}".format(i,i-len(s),x))
    i+=1