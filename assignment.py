


largest=None
smallest=None
num=input("Enter number :")
while True:
    if num=='done':
        break

    try:
        numi=int(num)
    except:
        print("Invalid")
    else:
      if smallest is None:
          smallest=numi
          largest=numi
      elif numi>largest:
          largest=numi
      elif numi<smallest:
          smallest=numi

print("Maximum is",largest)
print("Minimum is",smallest)
