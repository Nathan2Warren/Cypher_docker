#!/usr/bin/env python

def encrypt(text, key):
    encrypted = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            encrypted += chr((ord(char) + key-65) % 26 + 65)

        else:
            encrypted += chr((ord(char) + key - 97) % 26 + 97)

    return encrypted


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    data = input("Please enter text and key separated by a space: ").split()
    text = str(data[0])
    key = int(data[1])
    encrypted = encrypt(text, key)
    print(f'Original: {text}')
    print(f'Shift: {key}')
    print(f'Encrypted: {encrypted}')
