
array=list(map(int,input().split()))

n=len(array)
for i in range(1,n):
    for j in range(0,n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)