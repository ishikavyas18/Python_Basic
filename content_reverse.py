

# reverse internal content of string

s=input("Enter String: ")

word=s.split()
print(word)
l=len(word)
print(l)
l1=[]
for words in word:
    l1.append(words[::-1])

print(l1)
result=' '.join(l1)
print("Desired output : ",result)

