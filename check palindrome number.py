# Take input from the user
num = input("Enter a number: ")

# Reverse the number using slicing
reverse_num = num[::-1]

# Check if the number and its reverse are the same
if num == reverse_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
