#Guessing game on python

import random

#Introduction
print('Welcome to Python guessing game, Enjoy!!!')
print()

#Level Selection
while True:
    print('Select the level of game you want to play')
    print('(A) Easy \t (B)Medium \t (C) Hard \t (D) Exit game')
    level = input('Enter an option: ')

    if (level == 'a') or (level == 'A'):
        secretNumber = random.randint(1,10)
        print('You are playing the easy game')
        print()

        #Ask the player to guess six times
        for x in range(6, 0, -1):
            guess = int(input('Take a guess: '))
           
            #when the user gets it correctly
            if guess == secretNumber:
                print('You got it right with ' + str(x) + ' guess(es) left')
                break
            else:
                print('That was wrong')
                print(str(x) + ' guess(es) left')
                print()
                continue

    elif (level == 'b') or (level == 'B'):
        print('B')
    elif (level == 'c') or (level == 'C'):
        print('C')
    elif (level == 'd') or (level == 'D'):
        print('D')
    else:
        print('Please make a valid selection')
        print()
        print()
        continue
