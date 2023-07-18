def summation(low,high):
    total=0
    for i in range(low,high+1):
        total+=i
    return total 
op=summation(1,5)
print(op)