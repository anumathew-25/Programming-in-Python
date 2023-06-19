# File       :substringRemove.py
# Description:program to remove a particular substring from a string 
# Author     :Anu Mathew
# Date       :30-03-2023
string=input("Enter the string:")
substring=input("Enter the substring to be removed:")
newstring=""
if substring in string:
        newstring+=string.replace(substring,"")
        
print("The new string after the removal of the substring is : ",newstring)        
