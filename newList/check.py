# assume you have a list .check this list any given element present or not .


color = input("Enter your list (comma separated): ").split()
print(color)
search = input("Enter the element to search : ")

if search in color:
    print(f"{search} is present in the list.")
else:
    print(f"{search} is not present in this list.")