# File       :compare.py
# Description:program to compare two numbers
# Author     :Anu Mathew
# Date       :09-02-2023

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
if(x>y):
    print(x,"is greater than ",y)
elif(x<y):
    print(y,"is greater than",x)
else:
    print(x,"equals to ",y)        
