# This progarm will display the duty of every on in the family

print('WELCOME TO OUR DUTY ROASTER\n\n')
print('select an option from the following below:\n')
print('which of the follwoing role best suit you')
print('a. father \t\nb. mother \t\nc. children ')
print('***** please answer *****')
ans = input()
if ans == 'a':
       print('Did you give your wife money to go to the market?, (y/n)')
       a = input()
       print('Why cant struggle like other men?,(nothing/i cant)')
       a = input()
       print('Did you go to the office today? (y/n) ')
       a = input()
       print('what is your occupasion?, (lawyer/builder)')
       occupation = input()
       print('How was work today? (good/dull)')
       a = input()
       print('hope you really enjoyed it?, (y/n) ')
       a = input()
       if a == 'y':
              print('Ok you are a hard working man')
       elif a == 'lawyer':
              name = input()
              print('thats very good')
       elif a == 'builder':
              name = input()
              print('great builder association')
       elif a == 'n':
              print('put more effort')
       elif a == 'n':
              print('you cannot provide for you family')
       elif a == 'nothing':
              print('you are not serious')
       elif a == 'i cant':
              print('look at your self')    
       elif a == 'y':
              print('How was work today? (good/dull)')
       elif a == 'good':
              print('hope you really enjoyed it?, (y/n) ')
       elif a == 'y':
              print('thats good')
       elif a == 'n':
              print('dont worry the will soon open all the boader in this country')
       elif a == 'dull':
              print ('it is because of the coronavirus')
       elif a == 'n':
              print('You are a lazy man')
       else:
              print('Select the write option please\n')  
elif ans == 'b':
       print('Did you cook the food that your husband gave you money for it?, (y/n) ')
       b = input()
       if b == 'y':
              print('You are a wife materia')
       elif b == 'n':
              print('You are a lazy woman')
       else:
              print('You are not the person just go out\n')
elif ans == 'c':
       print('Did you people sweep the house?,(y/n) ')
       c = input()
       if c == 'y':
              print('You all have tried')
       elif c == 'n':
              print('What are you waiting for')
              print('Have you people clean the whole environment?, (y/n) ')
              c = input()
              if c == 'y':
                     print('Thats a very nice work')
              elif c == 'n':
                     print('You all are very lazy')
              else:
                     print('You are not sure of what you are saying')
