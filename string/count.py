# count no.of vowels,consonants and digits from a string
str =input("Enter the string:: ")
vowel=0
consonant=0
digit=0
str=str.lower()
for i in str:
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=="u"):
        vowel+=1
    elif(i>='0' and i<='9'):
        digit+=1
    else:
        consonant+=1
print("Number of vowels :: ",vowel)
print("Number of consonant:: ",consonant)
print("Number of digit:: ",digit)

