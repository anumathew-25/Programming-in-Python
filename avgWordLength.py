# File       :avgWordLength.py
# Description:program to find the number of characters in each word in a sentence and average word length
# Author     :Anu Mathew
# Date       :28-02-2023
string=input("Enter a sentence: ")
listOfWords=string.split()
sum=0
print("The words in the list are ",listOfWords)
for i in listOfWords:
    print(len(i))
    sum=sum+len(i)
print("Total Number of words: ",sum)
print("The average word length is ",sum/len(listOfWords))    