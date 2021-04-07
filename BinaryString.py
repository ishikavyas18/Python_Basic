
# to check if the given string is binary or not
def check(string):
    p=set(string)
    s={'0','1'}
    if s==p or p=={'0'} or p=={'1'}:
        print("yes")
    else:
        print("No")

s=input("Enter string:" )
#print(check(s))
check(s)