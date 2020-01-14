import re, pyperclip, onetimepad

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:" + "<>?,./" + "'" + '"' + ";" + " "

def ceaserCipher_encryption(plainMsg):
    # from random_number import plainMsg
    key = "5"
    encrypt_hex = ""
    key_itr = 0
    for i in range(len(plainMsg)):
        temp = ord(plainMsg[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0


    ceaserCipher_encryption.plain_enc = format(encrypt_hex)


def atBash_encryption(plainMsg):
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:" + "<>?,./" + "'" + '"' + ";"+" "
    # reversing alphabets of alpa variable
    rev_alpa = alpa[::-1]
    encry_text = ""
    for i in range(len(plainMsg)):
        if plainMsg[i] == chr(32):
            encry_text += " "
        else:
            for j in range(len(alpa)):
                if plainMsg[i] == alpa[j]:
                    encry_text += rev_alpa[j]
                    break
                # if
            # inner for
        # if-else
    # for

    atBash_encryption.plain_enc = format(encry_text)


def railFence_Cipher_encryption(plainMsg):
    rails = 5

    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(plainMsg)):
            railMatrix[row].append('.')
        # inner for
    # for

    # testing the matrix
    # for row in railMatrix:
    #     for column in row:
    #         print(column, end="")
    #     print("\n")
    #     # inner for
    # # for

    # putting letters of message one by one in the matrix in zig-zag
    row = 0
    check = 0
    for i in range(len(plainMsg)):
        if check == 0:
            railMatrix[row][i] = plainMsg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = plainMsg[i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else

    # testing the matrix with message in zig-zag
    # for row in railMatrix:
    #     for column in row:
    #         print(column, end="")
    #     print("\n")
    #     # inner for
    # # for

    encryp_text = ""
    for i in range(rails):
        for j in range(len(plainMsg)):
            encryp_text += railMatrix[i][j]
    # for

    # removing '.' from encrypted text
    encryp_text = re.sub(r"\.", "", encryp_text)
    railFence_Cipher_encryption.plain_enc = format(encryp_text)


def TransportationCipher_main(plainMsg):
    msg = plainMsg
    myKey = 5
    ciphertext = TransportationCipher_Message(myKey, msg)

    TransportationCipher_main.plain_enc = ciphertext



def TransportationCipher_Message(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)  # Cipher text


def XORcipher_encryption(plainMsg):
    msg = plainMsg
    key = "5"

    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0

    XORcipher_encryption.plain_enc = format(encrypt_hex)


def oneTimePad_encryption(plainMsg):
    cipher = onetimepad.encrypt(plainMsg, 'keypathhere')
    oneTimePad_encryption.plain_enc = cipher


def Autokey_EncryptionMain(plainMsg):
    message = plainMsg
    key = 'keypathhere'
    ontimepad_cipher = AutoKey_encryptMessage(message, key)
    Autokey_EncryptionMain.plain_enc = ontimepad_cipher


def AutoKey_encryptMessage(messages, keys):
    return AutoKey_cipherMessage(messages, keys)


def AutoKey_cipherMessage(messages, keys):
    cipher = []
    k_index = 0
    key = keys
    for i in messages:
        text = ALPHA.find(i)
        text += ALPHA.find(key[k_index])
        key += i  # add current char to keystream
        text %= len(ALPHA)

        k_index += 1

        cipher.append(ALPHA[text])
    return ''.join(cipher)

def ROT47cipher_encryption(plainMsg):
    message = plainMsg
    key = 5
    encryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encryp_text += " "
        elif temp > 126:
            temp -= 94
            encryp_text += chr(temp)
        else:
            encryp_text += chr(temp)

    ROT47cipher_encryption.plain_enc = format(encryp_text)

