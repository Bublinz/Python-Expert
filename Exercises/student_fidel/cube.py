# write a program the will compare the quality of two numbers and return the cube of their sum
def hello(we):
    print('This program will compare the quality of two number and return the cube of their sum')
    x = int(input('enter the first number: '))
    y = int(input('enter the second number: '))
    if x == y:
        sum = x + y
        cube = (sum *3)
        print('the cube of the number is ' + str (cube))
    elif x != y:
        print('they are not the same')
hello('we')
