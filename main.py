#Timothy Polkhovskiy's main code for their repository
encoded_password = []


def encode(password):
    list_password = []
    for x in password:
        x = int(x)
        list_password.append(x)
    for x in list_password:
        x += 3
        encoded_password.append(x)
    encoded_password_string = ''
    for x in encoded_password:
        x = str(x)
        encoded_password_string += x
    return encoded_password_string


while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    option = int(input("Please enter an option:"))
    if option == 1:
        password = input("Please enter your password to encode:")
        encode(password)
        print('Your password has been encoded and stored!')
    elif option == 2:
        pass
    elif option == 3:
        break
