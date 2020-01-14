# ROT47 Encryption
from generate_random import y


def demo_var4():
    from random_number import msg
    demo_var4.msg = msg


def cipher_encryption_rot47():
    # message = input("Enter message: ")
    key = 5
    msg = demo_var4.msg
    encryp_text = ""

    for i in range(len(msg)):
        temp = ord(msg[i]) + key
        if ord(msg[i]) == 32:
            encryp_text += " "
        elif temp > 126:
            temp -= 94
            encryp_text += chr(temp)
        else:
            encryp_text += chr(temp)
        # if-else
    # for
    # print("Encrypted Text: {}".format(encryp_text))
    cipher_encryption_rot47.unread = format(encryp_text)

    # Checking y[1]: index
    if y[1] == "two":
        from two_e import demo_var2, at_encryption
        demo_var2()
        demo_var2.msg = cipher_encryption_rot47.unread
        #    print(demo_var2.msg)
        at_encryption()
        print("Last4 Encrypted form of message pass through different file is:" + at_encryption.message)
    elif y[1] == "three":
        from three_e import demo_var3, cipher_encryption_rail
        demo_var3()
        demo_var3.msg = cipher_encryption_rot47.unread
        #    print(demo_var2.msg)
        cipher_encryption_rail()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_encryption_rail.unread)
    elif y[1] == "one":
        from one_e import demo_var1, cipher_encryption
        demo_var1()
        demo_var1.msg = cipher_encryption_rot47.unread
        # print(demo_var1.msg)
        cipher_encryption()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_encryption.unrea)
    elif y[1] == "five":
        from five_e import demo_var5, cipher_encryption_rot18
        demo_var5()
        demo_var5.msg = cipher_encryption_rot47.unread
        # print(demo_var1.msg)
        cipher_encryption_rot18()
        print("Last4 Encrypted form of message pass through different file is:" + cipher_encryption_rot18.unread)
    elif y[1] == "six":
        from six_e import cipher_encryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = cipher_encryption_rot47.unread
        # print(demo_var1.msg)
        cipher_encryption_xor()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_xor.xorunread)

