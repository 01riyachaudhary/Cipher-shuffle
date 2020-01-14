# At BAsh Encrytion

from Decryption import x


def demo_var2():
    from Decryption import msg
    demo_var2.msg = msg.upper()


def at_decryption():
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # reversing alphabets of alpa variable
    rev_alpa = alpa[::-1]
    msg = demo_var2.msg
    # msg = input("Enter msg: ").upper();
    dencry_text = ""

    for i in range(len(msg)):
        if msg[i] == chr(32):
            dencry_text += " "
        else:
            for j in range(len(rev_alpa)):
                if msg[i] == rev_alpa[j]:
                    dencry_text += alpa[j]
                    break
                    # if
                    # inner for
                    # if-else
    # for
    # print("Decrypted Text: {}".format(dencry_text))
    at_decryption.message = format(dencry_text)

    # Checking y[1]: index
    if x[1] == "one":
        from one_d import demo_var1, cipher_decryption
        demo_var1()
        demo_var1.msg = at_decryption.message
        # print(demo_var1.msg)
        cipher_decryption()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_decryption.unrea)

    elif x[1] == "three":
        from three_d import demo_var3, cipher_decryption_rail
        demo_var3()
        demo_var3.msg = at_decryption.message
        #    print(demo_var2.msg)
        cipher_decryption_rail()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_decryption_rail.unread)

    elif x[1] == "four":
        from four_d import demo_var4, cipher_decryption_rot47
        demo_var4()
        demo_var4.msg = at_decryption.message
        #    print(demo_var2.msg)
        cipher_decryption_rot47()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_decryption_rot47.unread)

    elif x[1] == "five":
        from five_d import demo_var5, cipher_decryption_rot18
        demo_var5()
        demo_var5.msg = at_decryption.message
        # print(demo_var1.msg)
        cipher_decryption_rot18()
        print("Last2 Encrypted form of message pass through different file is:" + cipher_decryption_rot18.unread)

    elif x[1] == "six":
        from six_d import cipher_decryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = at_decryption.message
        #    print(demo_var2.msg)
        cipher_decryption_xor()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_xor.xorunread)
