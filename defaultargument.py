# default argument

def printinfo(name,age=25):
    print('name',name)
    print('age',age)
    return 
#function call
printinfo(age=56,name='ali')
printinfo(name='ali')