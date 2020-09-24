# This program is a modified number guessing game
import random

print('welcome to your guessing game')
print('please select a level.')
print('a. easy\nb. medium\nc.hard')
ans = input()
if ans == 'a':
    easyguessing = random.randint(1,10)
    print('This is the easy level game')
    for apple in range(5,-1,-1):
        easy = int(input('guess a number:'))
        if easy == easyguessing:
            print('you got it right')
            break
        else:
            print('that was wrong')
            print('you have ' + str(apple) + ' guesses remaining')
    print('good bye')


elif ans == 'b':
    mediumguessing = random.randint(1,20)
    print('You are in the medium level game')
    for brown in range(3,-1,-1):
        medium = int(input('guess a number here:'))
        if medium == mediumguessing:
            print('you got it right')
            break
        else:
            print('that was wrong')
            print('you have ' + str(brown) + ' guesses remaining')
    print('good bye')

        
elif ans == 'c':
    hardguessing = random.randint(1,50)
    print('This is the hard level game')
    for hard in range(2,-1,-1):
        trust = int(input('take a guess:'))
        if trust == hard:
            print('you got it right')
            break
        else:
            print('that was wrong')
            print('you have ' + str(hard) + ' guesses left')
    print('good bye')
    
            
else:
    print('invalid input')
    print('game over')
    
        
