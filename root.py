# File       :root.py
# Description:program to find the square root of a quadratic equation
# Author     :Anu Mathew
# Date       :09-02-2023
import math
a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant value: "))
d=(b*b)-(4*a*c)
if(d==0):
    print("The square roots are equal")
    r=-b/(2*a)
    print("The square roots are ",r)
elif(d>0):
    print("The roots are real roots")
    r1=(-b+math.sqrt(d))/(2*a)  
    r2=(-b-math.sqrt(d))/(2*a) 
    print("The square roots are",round(r1,2),"and",round(r2,2)) 
else:
    print("The roots are imaginary roots")
