# print even length words in a string
str=input("Enter the string:: ")
# if(len(str)%2==0):
#     print(str)
# else:
#     print("it is not even string")

# another method
n=str.split()
for i in n:
    if(len(i)%2==0):
        print(i)
    else:
        print("it is not even string")

