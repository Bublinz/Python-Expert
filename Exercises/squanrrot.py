#A program to computer the sqaure root and cube root a numbers

count = 0
i = 1
while count !=9:
    print('Enter a number')
    num = int(input())
    squ = num * num
    cub = num * num * num
    print('==============================')
    print('Sn \t Square \t Cube')
    print(str(i) + "\t" + str(squ) + "\t" + str(cub))
    i = i + 1
    count = count + 1
print('Thank You')
