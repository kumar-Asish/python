# WAP to check if two string are Anagram or not.
str1=input("Enter the first string: ")
str2=input("Enter the second string:: ")
s1=sorted(str1)
s2=sorted(str2)
if(s1==s2):
    print(f"{str1} and {str2} is Anagram ")
else:
    print(f"{str1} and {str2} is not anagram")
