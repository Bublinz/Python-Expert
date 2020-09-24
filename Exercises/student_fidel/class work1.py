while True:
    print('enter your first name?')
    firstname = input()
    if firstname != 'Ugochi':
        continue
    else:
        break
while True:
    print('enter your last name?')
    lastname = input()
    if lastname != 'Sarah':
        continue
    else:
        break
while True:
    print('hello, Ugochi Sarah you are welcome.')
    print('please enter your email account?')
    email = input()
    if email != 'golDEn@gmail.com':
        continue
    else:
        break
while True:
    print('please enter your password')
    password = input()
    if len(password) >= 9:
        print('password received')
        break
    else:
        continue
    print('access granted')
