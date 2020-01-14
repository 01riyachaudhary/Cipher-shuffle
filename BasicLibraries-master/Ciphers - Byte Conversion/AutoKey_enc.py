ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_+-={}|[]\:"+"<>?,./"+"'"+'"'+";"+" "
print(ALPHA)
def main():
    message = input('enter message: ')
    key = 'keypathhere'
    cipher = encryptMessage(message, key)
    print(cipher)



def encryptMessage(messages, keys):
    return cipherMessage(messages, keys)

def cipherMessage (messages, keys):
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

if __name__ == "__main__":
    main()