#Timothy Polkhovskiy's main code for their repository

encoded_password = []   #Can use this to make your decoder shorter so you don't have to make a string to list
encoded_password_string = ''


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

def decode(encoded_password_string):
    decoded_password = ""

    for digit in encoded_password_string:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit

    return decoded_password

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
        encoded_password_string = encode(password)
        print('Your password has been encoded and stored!')
    elif option == 2:
        print(f'The encoded password is {encoded_password_string}, and the original password is {decode(encoded_password_string)}')
    elif option == 3:
        break
