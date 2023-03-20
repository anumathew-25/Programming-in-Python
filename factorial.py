# File       :factorial.py
# Description:program to find the factorial of a number
# Author     :Anu Mathew
# Date       :09-02-2023

fact=1
num=int(input("Enter the number: "))
for i in range(num):
    fact=fact*(i+1)
print("Factorial of",num,"is",fact)    

