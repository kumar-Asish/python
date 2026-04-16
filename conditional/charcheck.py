# check whether a character is alphabet ,digit or special characters
ch=input("Enter the character:: ")
ascii=ord(ch)
if(ascii>=48 and ascii<=57):
    print(f"{ch} is a number.")
elif(ascii>=65 and ascii<=90):
    print(f"{ch} is capital letter")
elif(ascii >=97 and ascii<=122):
    print(f"{ch} is small letter")
else:
    print(f"{ch} is specail character")
