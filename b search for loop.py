

#binary search using for loop
pos=-1
def search(list,key):
    lb=0
    ub=len(list)-1
    for i in range(len(list)):
        if lb<=ub:
            mid=(lb+ub)//2
            if list[mid]==key:
                globals()['pos']=mid
                return True
            else:
                if list[mid]<key:
                    lb=mid+1
                else:
                    up=mid-1
       # break
    return False
list=[4,56,78,99,455]
key=int(input("enter element to be found "))
if search(list,key):
    print("element found at : ",pos)
else:
    print("element not found")