string=input("Enter a string:")
words=string.split()
frequency={}
for item in words:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)        