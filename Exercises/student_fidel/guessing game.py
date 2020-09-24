# A python guessing program
import random
secretnumber = random.randint(1,50)
print('i am thinking of a number between 1 and 50\n')
# Ask the player to guess ten(10) times
for x in range(1,10):
    guess = int(input('take a guess: '))
    if guess < secretnumber:
        print ('your guess is too low')
    elif guess > secretnumber:
        print('your guess is too high')
    else:
        break # the program looping stops here
# when the user gets it correctly
if guess == secretnumber:
    print('good job you guessed my number in ' + str(x) + ' guesses')
else:
    print('nope the number i was thinking of was ' + str(secretnumber))
      
