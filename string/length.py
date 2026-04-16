# str=input("Enter the string:: ")
# s=len(str)
# print("Length of string is::-> ",s)

# without using len() function
def lengthstring(str):
    length=0
    for char in str:
        length+=1
    return length

str1=input("Enter the string:: ")
output=lengthstring(str1)
print("Length of the string is::-> ",output)

