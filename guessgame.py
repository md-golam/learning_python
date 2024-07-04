import random
print('what is your name?')
name = input()
print(' hello '+ name + ' lets play a guess game,guess a number between 1 to 20' )
secretnumber= random.randint(1,20)
for guessestkaen in range(1,7):
    print ('take a guess')
    guess=int(input())
    if guess< secretnumber:
        print("your guess is lower")
    elif guess > secretnumber:
        print("your guess is higher")
    else:
        break 
if guess == secretnumber: 
    print(' you guess the right number in ' + str(guessestkaen ) + ' times') 
else:
    print(' the number i guess was ' + str(guessestkaen))