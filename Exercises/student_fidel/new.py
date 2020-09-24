def Picnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 5, 'apples': 22, 'cups': 6, 'cookies': 10000}
Picnic(picnicItems, 12, 7)
Picnic(picnicItems, 20, 9)