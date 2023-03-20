# File       :digitSum.py
# Description:program to find the sum of digits of anumber
# Author     :Anu Mathew
# Date       :21-02-2023
num=int(input("Enter a number:"))
digit=0
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num//=10
print("The sum of digits of the number is",sum)    