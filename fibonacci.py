# File       :fibonacci.py
# Description:program to print the fibonacci series
# Author     :Anu Mathew
# Date       :25-02-2023
num=int(input("Enter the number of lines in the fibonacci series: "))
a=0
b=1
print("Fibonacci Serirs:")
print(a)
print(b)
for i in range(num-2):
    temp=a+b
    print(temp)
    a=b
    b=temp