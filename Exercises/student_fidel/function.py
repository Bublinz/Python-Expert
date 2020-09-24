import random
def GetAnswer(x):
    if x == 1:
        return 'this is the first number'
    elif x == 2:
        return 'this is the second number'
    elif x == 3:
        return 'this is the third number'
    elif x == 4:
        return 'this is the fourth number'
    elif x == 5:
        return 'this is the fifth number'
    elif x == 6:
        return 'this is the sixth number'
    elif x == 7:
        return 'this is the seventh number'
    elif x == 8:
        return 'this is the eight number'
    elif x == 9:
        return 'this is the nineth number'
    elif x == 10:
        return 'this is the tenth number'
    else:
        return 'no other number'
# r = random.randint(1,5)
# vivian = GetAnswer(r)
# print(vivian)
print(GetAnswer(random.randint(1, 10)))
    
# def greet(x):
#     print('hello ' +  x  +  ' you are welcome to my program')
# greet ('mikel')
# def Ans(x,y):
#     sum = x + y
#     Avg = sum /2
#     print('this is the sum: ' + sum)
#     print('this is the Avg: ' + Avg)    
    
