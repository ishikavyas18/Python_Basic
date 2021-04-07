

# program showing concept of binary search
pos=-1
def bSeacrh(list,n):
    low=0
    high=len(list)-1
    #i=0
    while low<=high:
        mid=(low+high)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                low=mid+1
            else:
                high=mid-1
    return  False

list=list(map(int,input().split(",")))
n=int(input("Enter key : "))
if bSeacrh(list,n):
    print("Elemnt found :",pos)
else:
    print("element not found")