def at_decryption():
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:"+"<>?,./" +"'"+'"'+";"+" "
    # reversing alphabets of alpa variable
    rev_alpa = alpa[::-1]

    message = input("Enter message: ")

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

    print("Decrypted Text: {}".format(dencry_text))


def main():
        at_decryption()


if __name__ == "__main__":
    main()