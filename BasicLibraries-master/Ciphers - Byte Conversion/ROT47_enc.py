def cipher_encryption():
    message = input("Enter message: ")
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
        # if-else
    # for
    print("Encrypted Text: {}".format(encryp_text))

def main():
        cipher_encryption()

if __name__ == "__main__":
    main()
