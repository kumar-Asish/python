# WAP to increament numeric string by n
num=input("enter the data:: ").split(' ')
digit='0123456789'
n=int(input("Enter the value of n:: "))
for i in range(len(num)):
    x=num[i]
    flag=True
    for ch in x:
        if ch not in digit:
            flag=False
            break
    if flag:
        num[i]=str(int(x)+n)
print("Updated list:: ",num)