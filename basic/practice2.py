# Program to increment numeric strings in a list by n without using isdigit()
num = input("Enter the data (space-separated): ").split(' ')
n = int(input("Enter the value of n: "))

# Define a string of digits
digits = '0123456789'

# Iterate over the input list
for i in range(len(num)):
    x = num[i]
    flag = True  # Assume the string is numeric
    for ch in x:
        if ch not in digits:  # Check if any character is not a digit
            flag = False
            break
    if flag:  # If all characters are digits
        num[i] = str(int(x) + n)

# Print the updated list
print("Updated list:", num)
