# File       :decToBin2.py
# Description:program to convert a decimal number to the binary number
# Author     :Anu Mathew
# Date       :25-02-2023
num=int(input("Enter a decimal number: "))
bin=""
while(num!=0):
    rem=num%2
    num=num//2
    bin=str(rem)+bin
print("The binary number is",bin)    

