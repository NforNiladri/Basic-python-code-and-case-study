import re
from cryptography.fernet import Fernet

# read Reference ID from command line
ref_id = input("Enter your Reference ID: ")

# check for validity - 12 digits and only numbers and alphabets
if re.match("^[a-zA-Z0-9]{12}$", ref_id) is None:
    print("Invalid Reference ID. Please enter a valid 12-digit Reference ID with only numbers and alphabets.")
    exit()

# encrypt the Reference ID
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(ref_id.encode())

# print the encrypted Reference ID
print("Encrypted Reference ID: ", cipher_text.decode())
