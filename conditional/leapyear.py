year=int(input("Enter the year:: "))
if(year % 4==0 and year !=100)or year % 400 ==0:
    print(f"{year} is leapyear")
else:
    print(f"{year} is not leapyear")
