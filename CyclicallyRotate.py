
arr=list(map(int,input().split()))

x=arr[-1]
#print(x)
n=len(arr)
for i in range(n-1,-1,-1):
    arr[i]=arr[i-1]
#print(arr)
arr[0]=x
print(arr)