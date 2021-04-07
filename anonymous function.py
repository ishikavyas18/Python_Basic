#filter reduce and map demo
from functools import reduce
print("filter demo :")
#def is_even(n):
   # return n%2==0
#n=None
nums=[2,34,4,57,90,99]
evens = list(filter(lambda p : p%2==0,nums))

double=list(map(lambda n:n*2,evens))

sum=reduce(lambda a,b:a+b ,double)
print(sum)
print(evens)
print("after doubling all the even values :",double)