
# bubble sort

def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
               # temp=list[j]
                #list[j]=list[j+1]
                #list[j+1]=temp
                list[j],list[j+1]=list[j+1],list[j]

       # break
list=[5,3,8,6,7,2]
print("unsorted list is :",list)
sort(list)
print("sorted list is :",list)
