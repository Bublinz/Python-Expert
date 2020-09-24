# write a python program that will calculate the number of days between two dates.
print('calculate the number of days between two dates')

def wind(count):
    a = int(input('enter the fisrt date: '))
    b = int(input('enter the second date: '))
    while a != b:
        sum = a - b
        print(str(int(sum)) +  ' days is the output left')
        break
    else:
        print('The are the same')
wind('count')
        