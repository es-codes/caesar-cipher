from utils.alphabet import alphabet

def encrypt_decrypt(direction_choice, plain_text, shift_amount):
    cipher_msg = ''
    for letter in plain_text:
        if letter not in alphabet:
            cipher_msg += letter
        else:
            position = alphabet.index(letter)
            if direction_choice == "encode":
                if position + shift_amount > 25:
                    cipher_msg += alphabet[position + shift_amount - 26]
                else:
                    cipher_msg += alphabet[position + shift_amount]     
            elif direction_choice == "decode":
                if position - shift_amount < 0:
                    cipher_msg += alphabet[position - shift_amount + 26]
                else:
                    cipher_msg += alphabet[position - shift_amount]
    if direction_choice != 'encode' and direction_choice != 'decode':
        print('Invalid direction')
        exit()
    print('----------------------------------')
    print(f'Your {direction_choice}d text is "{cipher_msg}"')
    print('----------------------------------')

