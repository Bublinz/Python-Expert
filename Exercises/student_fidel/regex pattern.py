import re
def get (find):
    print('enter your phone number: ')
    number = input()
    phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(number)
    print('Phone number found: ' + mo.group() )
get('mo')

