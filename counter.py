

# to count number of words and number of character in string

s=input("Enter string: ")

counter=0
wordcount=1
for i in s:

    if (i==' '):
        wordcount=wordcount+1
    counter = counter + 1
print("Total number of character is :",counter)
print("Total number of words: ",wordcount)