
# to check element found or not

d={'color':'red','model':'suv','year':8900}
element=input("Enter element to find:")
print(d)

if element in d.keys():
    print("Element found",element)
else:
    print("Element Not Found",element)
