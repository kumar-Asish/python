def safe_list_operation(lst, index):
    try:
        result = lst[index]
        print(f"Element at index {index}: {result}")
    except IndexError:
        print(f"Index {index} is out of range for the list.")

user_list = input("Enter a list of numbers separated by spaces: ").split()
user_list = [int(item) for item in user_list]

try:
    user_index = int(input("Enter the index you want to access: "))
    safe_list_operation(user_list, user_index)
except ValueError:
    print("Invalid input. Please enter a valid integer for the index.")