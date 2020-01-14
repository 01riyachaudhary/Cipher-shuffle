# At BAsh Encrytion
from generate_random import y


def demo_var2():
    from random_number import msg
    demo_var2.msg = msg.upper()


def at_encryption():
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    rev_alpa = alpa[::-1]
    msg = demo_var2.msg
    encry_text = ""

    for i in range(len(msg)):
        if msg[i] == chr(32):
            encry_text += " "
        else:
            for j in range(len(alpa)):
                if msg[i] == alpa[j]:
                    encry_text += rev_alpa[j]
                    break
                # if
            # inner for
        # if-else
    # for
    # print("Encrypted Text: {}".format(encry_text))
    at_encryption.message = format(encry_text)
    # print(at_encryption.message)

    # Checking y[1]: index

    if y[1] == "one":
        from one_e import demo_var1, cipher_encryption
        demo_var1()
        demo_var1.msg = at_encryption.message
        # print(demo_var1.msg)
        cipher_encryption()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_encryption.unrea)
    elif y[1] == "three":
        from three_e import demo_var3, cipher_encryption_rail
        demo_var3()
        demo_var3.msg = at_encryption.message
        #    print(demo_var2.msg)
        cipher_encryption_rail()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_encryption_rail.unread)
    elif y[1] == "four":
        from four_e import demo_var4, cipher_encryption_rot47
        demo_var4()
        demo_var4.msg = at_encryption.message
        #    print(demo_var2.msg)
        cipher_encryption_rot47()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_encryption_rot47.unread)
    elif y[1] == "five":
        from five_e import demo_var5, cipher_encryption_rot18
        demo_var5()
        demo_var5.msg = at_encryption.message
        # print(demo_var1.msg)
        cipher_encryption_rot18()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_encryption_rot18.unread)
    elif y[1] == "six":
        from six_e import cipher_encryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = at_encryption.message
        # print(demo_var1.msg)
        cipher_encryption_xor()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_xor.xorunread)
