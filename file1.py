# File       :file1.py
# Description:Python program to read a string from the keyboard and write it to a file and then read that string 
#             from the file and print it to the screen.
# Author     :Anu Mathew
# Date       :31-03-2023
str=input("Enter the string: ")
f=open("file1.txt",'w')
f.write(str)
f.close()
f=open("file1.txt",'r')
print(f.read())