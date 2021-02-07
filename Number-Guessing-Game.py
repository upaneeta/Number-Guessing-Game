import random 
number=random.randint(1,100)
flag=0
count=0
#number=36
while flag!=1:
    guess=int(input("\nGuess a no. Between 1 and 100\n"))
    count=count+1
    if guess>number:
        print("\nYou have to think of something lesser than this\nTry Again!")
    elif guess<number:
        print("\nYou have to think of something greater than this\nTry Again!") 
    else:
        print("\nCongratulations! You guessed it correct in "+ str(count) +" attempts!!\n\n\n  ")
        flag=1