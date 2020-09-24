import re
def you (the):
    i = 0
    while i < 4:
        i = i+1
        file = {'sarah':'girl'}
        glase = []
        print ('What is your name?')
        name = input()
        #for v in file.values():
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
        for i in range(len(number)):
            wind = re.compile(r'(\+\d\d\d\d-\d\d\d-\d\d\d\d)')
            be = wind.search(number)
            be = number[i:i+12]
            #if be(str(number)):
            #print('this is your phone number: ' + number)
            glase.append(name)
            glase.append(expression)
            glase.append(condition)
            glase.append(number)
            print('confirm your details before treatment:')
            print(glase)
    print(i)
you('the')

'''print ('yes' '/ ' 'no')
tick = input()
if tick == 'yes':
    print('go for treatment')
elif tick == 'no':
    print('ok')'''