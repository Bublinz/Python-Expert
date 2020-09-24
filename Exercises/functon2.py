import random

while True:
    unum1 = int(input('Enter your first number: ' ))
    if (unum1 < 1) or (unum1 > 20):
        continue
    else:
        break


while True:
    unum2 = int(input('Enter your second number: ' ))
    if (unum2 < 1) or (unum2 > 20):
        continue
    else:
        break

while True:
    unum3 = int(input('Enter your third number: ' ))
    if (unum3 < 1) or (unum3 > 20):
        continue
    else:
        break

num1 = random.randint(1,20)
print(num1)
num2 = random.randint(1,20)
print(num2)
num3 = random.randint(1,20)
print(num3)
 

if (num1==unum1) and (num2==unum2) and (num3==unum3):
    print('You have finally hit the jack Pot')
elif (num1==unum1) or (num2==unum2) or (num3==unum3):
    print('Ooops, thanks for your effort, try again later')
else:
    print('Go and read your book')