import re
print("My Calculator")
print("type 'quit' to exit\n")
run=True
previous=0

def do_math():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("Enter equation:")
    else:
        equation=input(str(previous))
    if equation=='quit':
        print("bye ")
        run=False
    else:
        equation=re.sub('[A-Za-z,;:()""]','',equation)
    if previous==0:
        previous=eval(equation)
    else:
        previous=eval(str(previous)+equation)
while run:
    do_math()