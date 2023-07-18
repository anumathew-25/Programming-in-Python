binary=input("Enter a binary number:")
decimal=0
expo=len(binary)-1
for digit in binary:
    decimal+=int(digit)*2**expo
    expo-=1
print("The decimal number is ",decimal) 
