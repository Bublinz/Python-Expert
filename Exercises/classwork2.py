#A program that uses the if statement and make some decision

print('WELCOME TO OUR QUIZE PLATFORM')
print()
print()
print('Select an option from the display below:::')
print()
print('What will you want us to do for you?')
print("a. Hack your System? \t b. Run an ending code in your laptop?")
print("c. Display students results \t d. Nothing!")
print("**** Answer Please ****")
ans = input()
if ans == 'a':
    aa = 0
    while aa <= 100:
        print('Idiot! Your system has been hacked!')
        print('Sorry, you cant do anything about it!')
        aa = aa + 1
elif ans == 'b':
    print('You are going to see unending code here, Are you sure (y/n)')
    bb = input()
    if bb == 'y':
        while True:
            print('010101010101010101010101010111010101010101010101010101010101010101010101001010101010')
    else:
        print('Good for you, Program tarminated')
        print('GoodBye!')
elif ans =='c':
    print('Here are the students result')
    print('Emeka \t A')
    print('Ebuka \t D')
    print('Chidera \t A')
    print('Monica \t C')
    print('Okoro \t A')
    print('Vivian \t B')
elif ans == 'd':
    print('You demanded we should do nothing, Goodbye')
else:
    print('Select a valid response')
    



