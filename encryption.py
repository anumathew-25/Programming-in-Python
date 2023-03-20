# File       :encryption.py
# Description:program to implement encryption of the ciper text
# Author     :Anu Mathew
# Date       :01-03-2023
string=input("Enter the text in small letters:")
distance=int(input("Enter the distance value: "))
code=""
for ch in string:
    ordValue=ord(ch)
    cipherValue=ordValue+distance
    if(cipherValue>ord('z')):
        cipherValue=(ord(ch)+distance-97)%26+97
    code+=chr(cipherValue)
print("Cipher Text: ",code)        
