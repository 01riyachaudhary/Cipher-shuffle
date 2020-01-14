import pyperclip


def main():
    msg = input('Enter your Text: ')
    myKey = 5
    ciphertext = encryptMessage(myKey, msg)


    print("Encrypted Test is:",ciphertext)
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)  # Cipher text


if __name__ == '__main__':
    main()