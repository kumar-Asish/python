def get_integer():
    try:
        num=int(input("enter the integer value:: "))
        print("you entered :: ",num)
    except ValueError:
        print("ERROR:Invalid input.Please enter a valid integer value")

get_integer()