def challenge(quiz):
    ContestantName = []
    x = 1
    while True:
        print('Enter the details of contestant ' + str(x))
        print('Enter your surname.')
        surname = input()
        if surname =='':
            break
        print('Enter your firstname.')
        firstname = input()
        print('How old are you')
        age = input()
        print('Who is the president of Nigeria')
        ans = input()
        if ans =='Robort Buhari':
            report='Good result'
            ContestantName =  ContestantName + [surname] + [firstname]+ [age] + [report]
            x = x+1
        else:
            ContestantName =  ContestantName + [surname] + [firstname]+ [age]
            print('you failed the quiz, good bye')
            break
            
        
    print('The Contestant Names are:')
    for details in ContestantName:
        print(' ' + details)
challenge('quiz')
