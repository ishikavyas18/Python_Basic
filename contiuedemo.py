#print all mumber from 1 to 20 but dont print value of number divisible by 3 or 5

for i in range(1,21):
    if i%3==0 and i%5==0:
        print("fizz")
        continue
    print(i)
print("bye")
