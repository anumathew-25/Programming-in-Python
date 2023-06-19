# File       :sumFile.py
# Description:Python program to read 10 numbers from the keyboard and write it to a file and then read that string 
#             from the file and print the sum of numbers to the screen.
# Author     :Anu Mathew
# Date       :31-03-2023
f=open("sumfile.txt",'w')
print("Enter the 10 numbers: ")
for i in range(10):
    num=input()
    f.write(num+'\n')
f.close()
sum=0
f=open("sumfile.txt",'r')
print("The numbers read from the file:")
while True:
    l=f.readline()
    if(l==""):
        break
    print(l.strip())
    num=int(l)
    sum+=num
print("Sum of numbers: ",sum)
f.close()
