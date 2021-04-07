
lst=[1,1,2,2,2,2,3]

x=int(input("Enter the number to count :"))
#count=0
n=len(lst)
def first_index(lst,low,high,x,n):
    if(high>=low):
        mid=low+high//2
        if((mid==0) or x>lst[mid-1]) and lst[mid]==x:
            return mid
        elif x>lst[mid]:
            return first_index(lst,mid+1,high,x,n)
        else:
            return first_index(lst,low,mid-1,x,n)
def last_index(lst,low,high,x,n):
    if(high>=low):
        mid=low+high//2
        if((mid==n-1) or x<lst[mid+1]) and lst[mid]==x:
            return mid
        elif x<lst[mid]:
            return last_index(lst,low,mid-1,x,n)
        else:
            return last_index(lst,mid+1,high,x,n)
def count_occurence(list,n,x):
    i=first_index(lst,0,n-1,x,n)
    j=last_index(lst,0,n-1,x,n)
    count=j-i+1
    return count
print(count_occurence(lst,x,n))