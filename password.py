# File       :password.py
# Description:2. Write a Python program to check the validity of a password given by the user (CO3, K3)
#               The Password should satisfy the following criteria:
#                   a. Contains at least one letter between a and z
#                   b. Contains at least one number between 0 and 9
#                   c. Contains at least one letter between A and Z
#                   d. Contains at least one special character from $, #, @
#                   e. Minimum length of password: 8
# Author     :Anu Mathew
# Date       :18-04-2023

password = input("Enter your password: ")

lowercase = False
uppercase = False
digit = False
special = False

for char in password:
    if char.islower():
        lowercase = True
    elif char.isupper():
        uppercase = True
    elif char.isdigit():
        digit = True
    elif char in ['$','#','@']:
        special = True

if lowercase and uppercase and digit and special and len(password) >= 8:
    print("Valid password")
else:
    print("Invalid password")


