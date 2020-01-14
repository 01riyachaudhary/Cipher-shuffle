from Decryption import x


def demo_var6():
    from Decryption import msg
    demo_var6.msg = msg

def cipher_decryption_xor():
    #msg = input("Enter message: ")
    key = "5"
    msg = demo_var6.msg
    hex_to_uni = ""
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i+2]).decode('utf-8')

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

    #print("Decrypted Text: {}".format(decryp_text))
    cipher_decryption_xor.xorunread=format(decryp_text)


    # Checking y[1]: index
    if x[1] == "one":
        from one_d import demo_var1, cipher_decryption
        demo_var1()
        demo_var1.msg = cipher_decryption_xor.xorunread
        # print(demo_var1.msg)
        cipher_decryption()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption.unrea)

    elif x[1] == "two":
        from two_d import demo_var2, at_decryption
        demo_var2()
        demo_var2.msg = cipher_decryption_xor.xorunread
        #    print(demo_var2.msg)
        at_decryption()
        print("Last5 Encrypted form of message pass through different file is:" + at_decryption.message)

    elif x[1] == "three":
        from three_d import demo_var3, cipher_decryption_rail
        demo_var3()
        demo_var3.msg = cipher_decryption_xor.xorunread
        #    print(demo_var2.msg)
        cipher_decryption_rail()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_rail.unread)

    elif x[1] == "four":
        from four_d import demo_var4, cipher_decryption_rot47
        demo_var4()
        demo_var4.msg = cipher_decryption_xor.xorunread
        #    print(demo_var2.msg)
        cipher_decryption_rot47()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_rot47.unread)

    elif x[1] == "five":
        from five_d import demo_var5, cipher_decryption_rot18
        demo_var5()
        demo_var5.msg = cipher_decryption_xor.xorunread
        # print(demo_var1.msg)
        cipher_decryption_rot18()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_decryption_rot18.unread)


