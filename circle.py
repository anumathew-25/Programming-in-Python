# File       :circle.py
# Description:program to find the area and circumference of a circle
# Author     :Anu Mathew
# Date       :09-02-2023

import math
radius=int(input("Enter the radius of the circle:"))
area=math.pi*radius*radius
circumference=2*math.pi*radius
print("Area of circle: ",round(area,2))
print("Circumference of the circle:",round(circumference,2))
