

s=input("Enter String: ")
output=''
lst=[]
#pre=''
for ch in s:
    if ch.isalpha():
        x = ch
       # output=output+ch

        #print(output)
    else:
        output=output+str(x*int(ch))
print(output)