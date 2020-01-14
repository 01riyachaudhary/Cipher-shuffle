def cipher_decryption():
    message = input("Enter message: ")
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

    print("Decrypted Text: {}".format(decryp_text))


def main():
    cipher_decryption()

if __name__ == "__main__":
    main()
