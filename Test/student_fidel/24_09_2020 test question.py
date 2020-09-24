import re
def power(letter):
    i = 0
    while (i < 4):
        i = i+1
        storage = {}
        glass = []
        print ('What is your name?')
        name = input()
        print ('How did the incident happened?')
        expression = input()
        print ('How is your condtion')
        print ('(a) not too bad (b) bad (c)very bad (d) worst')
        condition = input()
        if condition == 'a':
            print('Thanks for you information')
        elif condition == 'b':
            print('Thank god you are alive')
        elif condition == 'c':
            print('sorry for the accident that happened')
        elif condition == 'd':
            print('God is great for your live')
        else:
            print('It is not an option')
            continue
        print('please enter your phone number: ')
        number = input()
        contact = re.compile(r'(\+\d\d\d\d-\d\d\d-\d\d\d\d)')
        be = contact.search(number)
        glass.append(name)
        glass.append(expression)
        glass.append(condition)
        glass.append(number)
        print(glass)
power('letter')