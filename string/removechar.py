# write a user defined function to removing i-th character from a string
def remove(str,i):
    return str[:i]+str[i+1:]
string=input("Enter the string:: ")
n=int(input("Enter the position:: "))
output=remove(string,n)
print(output)