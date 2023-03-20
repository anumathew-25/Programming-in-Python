# File       :voddIndexRemove.py
# Description:program to remove characters in the odd index position from a string
# Author     :Anu Mathew
# Date       :17-03-2023

string=input("Enter a string:")
newString=""
for ch in string:
    ind=string.index(ch)
    if (ind%2==0):
        newString+=ch
print("The new String is",newString) 
