# File       :setOperations.py
# Description:Python program to do basic set operations
# Author     :Anu Mathew
# Date       :18-04-2023

# Get input from user for set A
a = set(input("Enter comma-separated elements for set A: ").split(","))

# Get input from user for set B
b = set(input("Enter comma-separated elements for set B: ").split(","))

# Union
union = a.union(b)
print("Union of set A and set B:", union)

# Intersection
intersection = a.intersection(b)
print("Intersection of set A and set B:", intersection)

# Difference
difference = a.difference(b)
print("Difference of set A and set B:", difference)

# Symmetric difference
symmetric_difference = a.symmetric_difference(b)
print("Symmetric difference of set A and set B:", symmetric_difference)
