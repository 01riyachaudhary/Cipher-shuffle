import re, onetimepad,math,sys

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:" + "<>?,./" + "'" + '"' + ";"+" "

def ceaserCipher_decryption(EncryptedMsg):
    # from random_number import EncryptedMsg
    msg = EncryptedMsg
    key = "5"

    hex_to_uni = ""

    for i in range(0, len(msg), 2):
        try:
            hex_to_uni += bytes.fromhex(msg[i:i + 2]).decode('utf-8')
        except:
            sys.exit()

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0

    ceaserCipher_decryption.plain_dec = format(decryp_text)


def atBash_decryption(EncryptedMsg):
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:" + "<>?,./" + "'" + '"' + ";"+" "
    # reversing alphabets of alpa variable
    rev_alpa = alpa[::-1]

    message = EncryptedMsg

    dencry_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            dencry_text += " "
        else:
            for j in range(len(rev_alpa)):
                if message[i] == rev_alpa[j]:
                    dencry_text += alpa[j]
                    break
                    # if
                    # inner for
                    # if-else
    # for

    atBash_decryption.plain_dec = format(dencry_text)


def railFence_Cipher_decryption(EncryptedMsg):
    msg = EncryptedMsg
    rails = 5

    # removing white space from message
    msg = msg.replace(" ", " ")

    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
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
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
                # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
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

    # reordering the matrix
    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                # skipping '.'
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1
            # if-else
        # inner for
    # for

    # testing matrix reorder
    for i in railMatrix:
        for column in i:
            print(column, end="")
        # inner for
        print("\n")
    # for

    # putting reordered matrix into decrypted text string to get decrypted text
    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(msg)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else
    # for

    decryp_text = re.sub(r"\.", "", decryp_text)
    railFence_Cipher_decryption.plain_dec = format(decryp_text)


def TransportationCipherDec_main(EncryptedMsg):
    msg = EncryptedMsg
    myKey = 5

    plaintext = TransportationCipherDec_Message(myKey, msg)
    TransportationCipherDec_main.plain_dec = plaintext


def TransportationCipherDec_Message(key, message):
    numOfColumns = int(math.ceil(len(message) / key))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1  # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


def XORcipher_decryption(EncryptedMsg):
    msg = EncryptedMsg
    key = "5"

    hex_to_uni = ""

    for i in range(0, len(msg), 2):
        try:
            hex_to_uni += bytes.fromhex(msg[i:i + 2]).decode('utf-8')
        except:
            sys.exit()

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0

    XORcipher_decryption.plain_dec = format(decryp_text)


def oneTimePad_decryption(EncryptedMsg):
    dec_msg = onetimepad.decrypt(EncryptedMsg, 'keypathhere')
    oneTimePad_decryption.plain_dec = dec_msg


def Autokey_DecryptionMain(EncryptedMsg):
    message = EncryptedMsg
    key = 'keypathhere'
    cipher = AutoKey_decryptMessage(message, key)
    Autokey_DecryptionMain.plain_dec = cipher


def AutoKey_decryptMessage(messages, keys):
    return AutoKey_DecCipherMessage(messages, keys)


def AutoKey_DecCipherMessage(messages, keys):
    cipher = []
    k_index = 0
    key = keys
    for i in messages:
        text = ALPHA.find(i)
        text -= ALPHA.find(key[k_index])
        key += ALPHA[text]  # add current char to keystream
        text %= len(ALPHA)

        k_index += 1

        cipher.append(ALPHA[text])
    return ''.join(cipher)


def ROT47cipher_decryption(EncryptedMsg):
    message = EncryptedMsg
    key = 5
    decryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) - key
        if ord(message[i]) == 32:
            decryp_text += " "
        elif temp < 32:
            temp += 94
            decryp_text += chr(temp)
        else:
            decryp_text += chr(temp)
            # if-else
    # for
    ROT47cipher_decryption.plain_dec = format(decryp_text)

