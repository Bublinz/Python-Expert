#write a program to get the largest number from a list
print('This program get the largest and smallest number from a list')

Ben = [23,15,13,36,18,3,14,76,25,12]

def module(calculate):
    mx = max(Ben)
    mi = min(Ben)
    rg = mx-mi
    if mx==mi:
        return str(mx) + ' is equal to ' + str(mi) + ' and range is: ' + str(rg)
    else:
        return 'the largest number is: ' + str(mx) + '\nwhile the smallest number is: ' + str(mi)
module('calculate')
    
