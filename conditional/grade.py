num=int(input("Enter the marks:: "))
if(num >=90 and num<=100):
    print("You got 'A' grade")
elif(num >=80 and num <90):
    print("You got 'B' grade")
elif(num >=70 and num <80):
    print("You got 'C' grade")
elif(num >=60 and num <70):
    print("You got 'D' grade")
elif(num>100):
    print("Enter valid number")
else:
    print("You are Fail,better luck next time")
