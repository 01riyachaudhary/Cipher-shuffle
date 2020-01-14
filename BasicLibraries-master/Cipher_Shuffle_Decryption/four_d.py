# ROT47 Decryption
from Decryption import x


def demo_var4():
    from Decryption import msg
    demo_var4.msg = msg

def cipher_decryption_rot47():
    #msg = input("Enter msg: ")
    key = 5
    msg = demo_var4.msg
    decryp_text = ""

    for i in range(len(msg)):
        temp = ord(msg[i]) - key
        if ord(msg[i]) == 32:
            decryp_text += " "
        elif temp < 32:
            temp += 94
            decryp_text += chr(temp)
        else:
            decryp_text += chr(temp)
            # if-else
    # for

   # print("Decrypted Text: {}".format(decryp_text))
    cipher_decryption_rot47.unread = format(decryp_text)

    # Checking y[1]: index
    if x[1] == "two":
        from two_d import demo_var2, at_decryption
        demo_var2()
        demo_var2.msg = cipher_decryption_rot47.unread
        #    print(demo_var2.msg)
        at_decryption()
        print("Last4 Encrypted form of message pass through different file is:" + at_decryption.message)

    elif x[1] == "three":
        from three_d import demo_var3, cipher_decryption_rail
        demo_var3()
        demo_var3.msg = cipher_decryption_rot47.unread
        #    print(demo_var2.msg)
        cipher_decryption_rail()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_decryption_rail.unread)

    elif x[1] == "one":
        from one_d import demo_var1, cipher_decryption
        demo_var1()
        demo_var1.msg = cipher_decryption_rot47.unread
        # print(demo_var1.msg)
        cipher_decryption()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_decryption.unrea)

    elif x[1] == "five":
        from five_d import demo_var5, cipher_decryption_rot18
        demo_var5()
        demo_var5.msg = cipher_decryption_rot47.unread
        # print(demo_var1.msg)
        cipher_decryption_rot18()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_decryption_rot18.unread)

    elif x[1] == "six":
        from six_d import cipher_decryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = cipher_decryption_rot47.unread
        #    print(demo_var2.msg)
        cipher_decryption_xor()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_xor.xorunread)


