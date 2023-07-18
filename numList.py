num=int(input("Enter the number of elements in the list:"))
print("Enter the elements in the list:")
posList=[]
negList=[]
for i in range(num):
    element=int(input())
    if(element>=0):
        posList.append(element)
    else:
        negList.append(element)
print("Positive Number List:",posList)  
print("Negative Number List:",negList)          
