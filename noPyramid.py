# File       :noPyramid.py
# Description:program to print th following pattern
#               1
#               2   2 
#               3   3   3
# Author     :Anu Mathew
# Date       :17-02-2023

num=int(input("Enter the number of lines: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()    