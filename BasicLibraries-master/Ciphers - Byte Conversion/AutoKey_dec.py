ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:"+"<>?,./" +"'"+'"'+";"+" "

def main():
    message = input('enter message: ')
    key = 'keypathhere'
    cipher = decryptMessage(message, key)
    print(cipher)



def decryptMessage(messages, keys):
    return cipherMessage(messages, keys)



def cipherMessage (messages, keys):
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

if __name__ == "__main__":
    main()