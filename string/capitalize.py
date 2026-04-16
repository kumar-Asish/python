str=input("Enter the string:: ")
str=str.title()
str=str.split()
str2=""
for i in str:
    str2=str2+i[:-1]+i[-1].upper()+" "
print(str2)