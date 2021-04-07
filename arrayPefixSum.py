
lst=list(map(int,input().split(",")))

print("Enter list is: ",lst)

q=int(input("Enter total number of queries :"))
j=0
while(j<q):
    l = int(input("Enter left index: "))
    r = int(input("Enter right index: "))
    sum = 0
    i = lst[0]

    while (l <= r):
        i = l
        sum = sum + lst[i]
        l = l + 1
    print("sum between left index and right index is: ", sum)
    j=j+1
