# File       :oddEven.py
# Description:program to find the even andd odd numbers in a given set of numbers
# Author     :Anu Mathew
# Date       :25-03-2023
limit=int(input("Enter the limit of the set:"))
even=[]
odd=[]
print("Enter th numbers in the set:")
for i in range(limit):
    num=int(input())
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)     
print("Even:",even) 
print("Odd:",odd)   