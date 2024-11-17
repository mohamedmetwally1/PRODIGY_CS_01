letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_decrypt(text, mode, key):
    result = ''
    num_letters = len(letters)  # Define the length of the alphabet

    if mode == 'd':  # If decrypting, reverse the key
        key = -key

    for letter in text:
        letter = letter.lower()
        if letter == ' ':  # Keep spaces unchanged
            result += ' '
        else:
            index = letters.find(letter)
            if index == -1:  # Handle non-alphabetic characters
                result += letter
            else:
                new_index = (index + key) % num_letters
                result += letters[new_index]
    return result

print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')
else:
    print('Invalid input! Please enter "e" for encrypt or "d" for decrypt.')
