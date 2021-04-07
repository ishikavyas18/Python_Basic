# Example shows the custom generator function

# it basically works between range of two values

# print the value between 1 to 100
# print even numbeer betwwen 1 to 100

def customgen(x, y):
    while (x <= y):
        # this if will print even number between 1 to 100
        if (x % 2 == 0):
            yield x
        x += 1


a = customgen(1, 100)
for number in a:
    print(number)
