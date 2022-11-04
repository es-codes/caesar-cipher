from utils.art import logo
from utils.helper import encrypt_decrypt

print(f'{logo}')
print('Welcome to Caesar Cipher!\n')
print('---------------------------------------------------------------------')

leave = ''
while leave != 'yes':
    encrypt_decrypt(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"), input("Type your message:\n").lower(), int(input("Type the shift amount number:\n")))
    leave = input('Do you wish to leave ? (type "yes" to leave or "no" to stay)')
    if leave == 'yes':
        print('----------------------------------------')
        print('Thanks for using Caesar Cipher. Goodbye!')





