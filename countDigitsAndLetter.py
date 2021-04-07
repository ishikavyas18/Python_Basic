
# program to count number of digits and letter present in a string:

s=input("Enter an alphanumberic string: ")
dcount=0
lcount=0
for ch in s:
    if ch.isalpha():
        lcount=lcount+1
    elif ch.isdigit():
        dcount=dcount+1

print("Count of letters: ",lcount)
print("Count of digits: ",dcount)
