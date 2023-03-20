# File       :palindrome.py
# Description:program to check whether a string is a palindrome or not
# Author     :Anu Mathew
# Date       :25-02-2023
str=input("Enter a string: ")
rev=str[::-1]
if(str==rev):
    print("This is a Palindrome")
else:
    print("This is not a palindrome")    