# Take input from the user
input_str = input("Enter a sentence: ")

# Initialize the letter and digit counters to zero
num_letters = 0
num_digits = 0

# Loop through each character in the input string
for char in input_str:

    # Check if the character is a letter using isalpha() method
    if char.isalpha():
        num_letters += 1

    # Check if the character is a digit using isdigit() method
    elif char.isdigit():
        num_digits += 1

# Print the results
print("LETTERS:", num_letters)
print("DIGITS:", num_digits)
