

# continue demo

number=[10,20,0,5,0,3]

for i in number:
    if i==0:
        print("numvber is zero so skipping")
        continue
    print("100/{}={}".format(i,100/i))