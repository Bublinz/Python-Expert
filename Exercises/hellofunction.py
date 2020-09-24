import random
def getAnswers(answerNumber):
    if answerNumber == 1:
       return 'Is is certain'
    elif answerNumber == 2:
        return 'Not vey certain'
    elif answerNumber == 3:
        return 'Not sure of answer'
    elif answerNumber == 4:
        return 'vey certain'
    elif answerNumber == 5:
        return 'Not answer'
    elif answerNumber == 6:
        return 'Not certain'
    elif answerNumber == 7:
        return 'sure answer'
    elif answerNumber == 8:
        return 'Dont take certainty'
    elif answerNumber == 9:
        return 'Not corona'
    else:
        return 'inclonclusive'
   
#r = random.randint(1, 9)
#fortune = getAnswers(r)
print('Enter a number')
a = int(input())
fortune = getAnswers(a)
print(fortune)
