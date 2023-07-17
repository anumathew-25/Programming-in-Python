import random
smallest=int(input("Enter the smallest limit:"))
largerst=int(input("Enter the largest limit:"))
myNo=random.randint(smallest,largerst)
count=0
while True:
    count+=1
    userGuess=int(input("Enter your guess:"))
    if(myNo<userGuess):
        print("Too big!")
    elif(myNo>userGuess):
        print("Too small")
    else:
        print("Congratulations!!You are guessed right!You got it in",count,"tries")
        break