import random


print('Please guess a number between 1 and 10')
yourNum = input()
randomNum = str(random.randint(1,10))

while yourNum != randomNum :

    if yourNum < randomNum :
        print('Your number was too low!! Guess again!')
        yourNum = input ()
        
    elif yourNum > randomNum :
        print ('Your number was too high!! Guess again!')
        yourNum = input ()
else : 
    print('Wow you guessed it right!!')

