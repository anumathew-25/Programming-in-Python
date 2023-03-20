# File       :vowelsRemove.py
# Description:program to remove the vowels in a string
# Author     :Anu Mathew
# Date       :17-03-2023
str=input("Enter a string :")
newStr=""
vowels="aeiouAEIOU"
for ch in str:
    if ch not in vowels:
        newStr+=ch
print("New String is ",newStr)
