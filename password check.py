# Take input from the user
password = input("Enter a password: ")

# Define a list of valid special characters
special_chars = ['$', '#', '@']

# Initialize the validity flag to False
valid_password = False

# Check if the password meets all criteria
if len(password) >= 6 and len(password) <= 12:
    if any(char.islower() for char in password):
        if any(char.isdigit() for char in password):
            if any(char.isupper() for char in password):
                if any(char in special_chars for char in password):
                    valid_password = True

# Print the result
if valid_password:
    print("Valid password")
else:
    print("Invalid password")
