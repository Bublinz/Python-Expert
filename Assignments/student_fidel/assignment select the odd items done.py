# write a program to select the odd item of a list
print('This program will select the odd item of a list')

def remove_even(l):
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    print (l)
    return l

remove_even([1,2,3,4,7,8,5,9,4,13,18])
remove_even([4,5,4,7,9,11,13,14,15,16,17])
remove_even([4,3,6,5,4,7,9,11,12,13])

