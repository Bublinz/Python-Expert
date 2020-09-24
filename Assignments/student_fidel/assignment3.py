# welcome to our  office.
while True:
    print('what is your name?')
    name = input()
    if name != 'vicTOria':
        continue
    print('hello, vicTOria you are welcome.')
    print('please enter your email account?')
    email = input()
    if email != 'ViCtOrIa@gmail.com':
        continue
    print('please enter your password')
    password = input()
    if len(password) >= 8:
        print('successfully granted')
        print('how old are you? ')
        age = input ()
        print('you will be ' + str(int(age)+1) + ' next years')
        print('where are you from? ')
        address = input ()
        print('what is the name of your best friend')
        name = input ()
        print('what is your occupation? ')
        occupation = input ()
        print('what is your complexion')
        complexion = input()
        print('request granted')
        break
                     
    
    
