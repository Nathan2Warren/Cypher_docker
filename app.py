#!/usr/bin/env python
import click

@click.command()
@click.option('--text', type = str)
@click.option('--key', type = int)

def encrypt(text = 'blank', key = '2'):
    encrypted = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            encrypted += chr((ord(char) + key-65) % 26 + 65)

        else:
            encrypted += chr((ord(char) + key - 97) % 26 + 97)
            
    print(f'Original: {text}')
    print(f'Shift: {key}')
    print(f'Encrypted: {encrypted}')


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    encrypt()

