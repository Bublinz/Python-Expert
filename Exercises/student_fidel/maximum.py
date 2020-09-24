# This program will display the maximum, minimum and range of given numbers

x = int(input('enter the first number: '))
y = int(input('enter the second number: '))

mx = max(x, y)
mi = min(x, y)
rg = mx-mi
if mx==mi:
    print(str(mx) + ' is equal to ' + str(mi) + ' and range is: ' + str(rg))
else:
    print('the maximum is: ' + str(mx) + ' while the minimum is: ' + str(mi) + ' and range is: ' + str(rg))
    
