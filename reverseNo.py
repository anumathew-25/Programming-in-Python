# File       :reverseNo.py
# Description:program to reverse a number
# Author     :Anu Mathew
# Date       :21-02-2023

num=int(input("Enter a number: "))
digit=0
reverse=0
while(num!=0):
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("The reverse of the number is ",reverse)    