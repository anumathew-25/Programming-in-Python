# File       :noPattern.py
# Description:program to print th following pattern
#               1
#               1   2 
#               1   2   3
# Author     :Anu Mathew
# Date       :17-02-2023

num=int(input("Enter the number of lines: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")#this is used to print the numbers in same line with a space
    print() #to print in next line   
