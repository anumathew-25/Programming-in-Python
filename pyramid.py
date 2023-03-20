# File       :pyramid.py
# Description:program to print  different types of  patterns
#            *
#            **
#            ***
#            ****
# Author     :Anu Mathew
# Date       :17-02-2023

num=int(input("Enter the number of lines of the pyramid: "))
print("Pattern 1:")
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

print("Pattern 2:")
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
