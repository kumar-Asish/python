def sumofnumber(n):
    if(n==1):
        return n
    return sumofnumber(n-1)+n
num=int(input("Enter the number:: "))
print(f"sum of {num} natural number is:: ",sumofnumber(num))
