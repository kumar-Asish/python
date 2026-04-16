# WAP to find the sum of character of ASCII value in string list
num=[]
n=int(input("Enter the no.of elements:: "))
for i in range (n):
    ele=input("Enter the element :: ")
    num.append(ele)
print("The list is::",num)
new=[]
for j in num:
    sum=0
    for k in j:
        sum=sum+ord(k)
    new.append(sum)
print("The sum of ASCII value is:: ",new)