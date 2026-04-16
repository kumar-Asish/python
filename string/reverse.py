# first approch
# str=input("enter the string:: ")
# rev=str[::-1]
# print(rev)

# second approch
str=input("Enter the string:: ")
rev=''
for char in str:
    rev=char+rev
print(rev)