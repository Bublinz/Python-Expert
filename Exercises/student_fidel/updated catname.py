CatName=[]
while True:
    print('Enter the name of cat ' + str(len(CatName)+1) + ' (or enter nothing to stop)')
    name = input()
    if name == 'donkey':
        break
    CatName = CatName + [name] # list concatenation
print('The CatNames are:')
for name in CatName:
    print(' ' + name)
