''' welcome to the house of strong security '''
while True:
    print("Enter your name:")
    name = input()
    if name.isalpha():
        continue
    else:
        if name.isalnum():
            print("hello, " + name + " nice to meet you")
            print("how are you doing")
            feeling = input()
            print("i feel " + feeling + " too ")
            print('please enter your email account?')
            email = input()
            if email != 'pasSWoRd@gmail.com':
                continue        
            print("please enter your password(letters and numbers are needed only):")
            password = input()
            if password.isdecimal():
                    print("passwords are letters and numbers please repeat")
                    continue
            else:
                if password.isalnum():
                    print ("the length of your password is ")
                    print (len(password))
                    print("access granted")
                    print("you can now come inside")
                    break
print()
print("my detail" "\n")
print("my name is " + name + "\ni feel " + feeling + " thanks\nmy email address is " + email + " then\nmy password is " + password + " thanks")

                                                           
