
# binary serach

pos=-1
def search(list,key):
    lb=0
    ub=len(list)-1
    while lb<=ub:
        mid=(lb+ub)//2
        if list[mid]==key:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<key:
                lb=mid+1
            else:
                ub=mid-1

    return False



list=list(map(int,input().split(",")))
key=int(input("Enter element to be found :"))

if search(list,key):
    print("element found",pos)
else:
    print("elemnet not found")