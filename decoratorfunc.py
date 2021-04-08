# example showing decorator function

# define a decore function

def decore(fun):
    def inner():
     #body of decorator function
        result=fun()
        return result*4
    return inner()

#now defining the function which will be decorated

def num():
    return 9

# now invoke the decorator function

resultfun=decore(num)
print(resultfun)
