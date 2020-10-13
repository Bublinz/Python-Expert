import re
def Tail(see):
    mentor = {}
    apprentice = []
    z = 0
    while (z < 7):
        z = z+1
        print('write your name:')
        name = input()
        print('Are you a male or a female?')
        indicate = input()
        if indicate == 'male':
            print()
        if indicate == 'female':
            print()
        print('what is your phone number: ')
        N = input()
        number = re.compile(r'(\+\d\d\d\d-\d\d\d-\d\d\d\d)')
        be = number.search(N)
        apprentice.append(name)
        apprentice.append(indicate)
        apprentice.append(N)
        print(apprentice)
Tail('see')


