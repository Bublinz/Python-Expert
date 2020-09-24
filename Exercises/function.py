import random
def greet(x):
     print ('hello ' + x + ' you are welcome to my program')
#greet('benita')
def answer(x,y):
    sum = x + y
    avg = sum/2
    #print('this is the sum ' + str(sum))
    #print('this is the average ' + str(avg))
    return()
#answer(4,2)

def getAnswer(x):
    if x == 1:
        return 'this is the first number'
    elif x == 2:
        return 'this is the second number'
    elif x == 3:
        return 'this is the third number'
    elif x == 4:
        return 'this is the fourth number'
    else:
        return 'this is the fifth number'

#r = random.randint(1,5)
#benita = getAnswer(r)
#print(benita)

print(getAnswer(random.randint(1,5)))

