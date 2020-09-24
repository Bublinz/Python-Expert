
def collatz (number):
    print(number)
    while True:
        if number == 1:
            print('end the program')
            break
        
        elif number % 2 == 0:
            number = number//2
            print(number)
        else:
            number = 3*number + 1
            print(number)
        if number != 1:
            continue

        
num = int(input('please enter a number:'))
print(collatz(num))
