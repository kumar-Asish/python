# WAP to input string in uppercase and convert half of string to lowercase .
# str=input("Enter the string :: ")
# str=str.upper()
# n=(len(str)//2)
# r=str[:n]+str[n:].lower()
# print(r)

# second apporch
str=input("Enter the string:: ")
hs=len(str)//2
str2=""
for i in range(len(str)):
    if i < hs:
        str2=str2+str[i].upper()
    else:
        str2=str2+str[i].lower()
print(str2)
