def cipher_encryption():
    msg= input("Enter message: ")
    #from random_number import msg
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

    print("Encrypted Text: {}".format(encrypt_hex))



def choose():
    cipher_encryption()

if __name__ == "__main__":
    choose()

