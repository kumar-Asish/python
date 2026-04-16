num=int(input("enter the number:: "))
for i in range(1,num+1):
    print("")
    for j in range(1,num+1):
        a=(num//2)+1
        if i==a or i==a-1 or j==a or j==a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
# print(" ",end=" ")
