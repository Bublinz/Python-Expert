import copy
def eggs(someparameter):
    someparameter.append('hello')
spam = [1,2,3]
eggs(spam)
print(spam)

spam = [int('3' * 2)/ 11]
print(spam)
spam = ['A','B','C','D']
cheese = copy.copy(spam)
cheese[1] = 42
print(cheese)

eggs = ('hello', 42, 0.5)
eggs[0]
print(eggs)
eggs = [1,2,3]
eggs = [4,5,6]
del eggs[:-3]
print(eggs)
