import telephone_number

def main():
    phone_number = input('Enter your telephone number: ')

    while not phone_number.valid_telephone_number(telephone_number):  
        print('That number is invalid.')
        phone_number = input('Enter your telephone number: ')

    print('That is a valid entry.')

main()