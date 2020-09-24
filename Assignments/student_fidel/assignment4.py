print('who are you?')

def guide(let):
    name = input()
    while True:
        if name != 'Destiny':
            continue
        print('Hello, Destiny nice to meet you')
        print('what is your age ?')
        age = input()
        print('you are going to be ' + str(int(age)+1) + ' next year')
        print('please enter your email account?')
        email = input()
        if email != 'golDEn@gmail.com':
            continue
        print('please enter your password')
        password = input()
        if password == 'DesTinY':
            print('successfully granted')
            print('password received')
            break
guide('let')



    
