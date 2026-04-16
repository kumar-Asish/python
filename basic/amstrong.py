num=int(input("enter the number:: "))
temp=num
base=0
while(num>0):
    rem=num%10
    num=num/10
    base=base+(rem*rem*rem)
if(temp==base):
    print("input number is armstrong number")
else:
    print("input number is not armstrong number")

