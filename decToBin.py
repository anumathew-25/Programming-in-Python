# File       :decToBin.py
# Description:program to convert a decimal number to the binary number
# Author     :Anu Mathew
# Date       :21-02-2023
num=int(input("Enter a decimal Number: "))
binary=0
ctr=0
temp=num
while(temp>0):
    binary=((temp%2)*(10**ctr))+binary
    temp=int(temp/2)
    ctr+=1
print("Binary Number: ",binary)    