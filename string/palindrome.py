#first approch
# str1=input("Enter the string:: ")
# str2=str1[-1: :-1]
# if(str1==str2):
#     print(f"{str1} is palindrome")
# else:
#     print(f"{str1} is not palindrome")

#second approch
str1=input("Enter the string :: ")
rev=''
for char in str1:
    rev=char+rev
if str1==rev:
    print(f"{str1} is palindrome")
else:
    print(f"{str1} is not palindrome")

