# Create an empty list to store the even-digit numbers
even_digit_nums = []

# Loop through all numbers from 1000 to 3000 (both inclusive)
for num in range(1000, 3001):

    # Convert the number to a string for digit-wise access
    str_num = str(num)

    # Check if all digits are even
    if int(str_num[0]) % 2 == 0 and int(str_num[1]) % 2 == 0 and int(str_num[2]) % 2 == 0 and int(str_num[3]) % 2 == 0:
        even_digit_nums.append(str_num)

# Print the even-digit numbers as a comma-separated sequence on a single line
print(",".join(even_digit_nums))
