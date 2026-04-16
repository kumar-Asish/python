# find the location of any given word in a string 
str=input("Enter the string::: ")
target=input("Enter the word which location you found:: ")
count=1
k=str.split()
for i in k:
    if(target==i):
        print("The location of this word:: ",count)
    else:
        count+=1