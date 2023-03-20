# File       :reverse.py
# Description:Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# Author     :Anu Mathew
# Date       :28-02-2023
firstName=input("Enter your first name: ")
lastName=input("Enter your last name: ")
fName=firstName[-1::-1]
lName=lastName[-1::-1]
print("Your Name in Reverse:",lName,fName)