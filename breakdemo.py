#break

availabe=5
x=int(input("enter candies :"))
i=1
while i<=x:
    print("candies")
    if i>availabe:
        print("out of stock !!")
        break
    i+=1
print("get lost")
