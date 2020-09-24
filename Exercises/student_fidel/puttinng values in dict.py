kind = {'ben':'sarah'}
details = []

while True:
    print('Enter your name')
    name = input()
    if name == "":
        break
    else:
        for k in kind.keys():
            if name == k: 
                print('It is already existing')
                continue
            else:
                print('how old are you')
                age = int(input())
                print('what is your complexion?')
                complexion = input()
                print('what is your height? ')
                height = int(input())
                print('what is your occupation')
                occupation = input()
                print('where are you from')
                address = input()
                print('who is your best friend')
                bestfriend = input()
                details.append(age)
                details.append(complexion)
                details.append(height)
                details.append(occupation)
                details.append(address)
                details.append(bestfriend)
                print(details)
                kind[name] = details
                break
    continue
print(kind)
