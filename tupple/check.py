color=input("Enter the color name:: ").split()
b=tuple(color)
print(b)
search =input("Enter the search element:: ")
if search in b:
    print (f"YES ! {search} is present")
else:
    print(f"NO ! {search} is not present")