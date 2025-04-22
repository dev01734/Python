import random 
a=-1
n = random.randint(0,10)
guesses = 1
while(a!=n):
    a= int(input("Enter a No computer Guess: "))
    if(a>n):
        print("Get lower")
    elif(a<n):
        print("Get Higher")
    guesses+=1
print(f'You have guessed {n} number correctly in {guesses} guesses')

