number = input('Enter your telephone number: ')
def telephone(check):
    length = False
    hyphens = False
    digits = False

    if len(check) == 12:
        length = True

    for be in check:
        if be [3, 7] == '-':
            hypens = True
        if be.isdigit():
            digits = True

    if length and hypens and digits:
        valid = True
    else:
        valid = False

    print (valid)