
def at_encryption():
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:"+"<>?,./" +"'"+'"'+";"+" "
    # reversing alphabets of alpa variable
    rev_alpa = alpa[::-1]
    print(rev_alpa)
    message = input("Enter message: ")
    encry_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            encry_text += " "
        else:
            for j in range(len(alpa)):
                if message[i] == alpa[j]:
                    encry_text += rev_alpa[j]
                    break
                # if
            # inner for
        # if-else
    # for

    print("Encrypted Text: {}".format(encry_text))

def main():

        at_encryption()


if __name__ == "__main__":
    main()