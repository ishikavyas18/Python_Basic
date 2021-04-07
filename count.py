

#count value


s=input("Enter String: ")

previous=s[0]
count=1
i=1
output=""
while i<len(s):
    if s[i]==previous:
        count=count+1
    else:
        output=output+str(count)+previous
        previous=s[i]
        count=1
    if i==len(s)-1:
        output=output+str(count)+previous
        count=1
    i=i+1
print(output)