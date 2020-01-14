# ROT18 Encryption
import re
from Decryption import x


def demo_var5():
    from Decryption import msg
    demo_var5.msg = msg.upper()


def cipher_decryption_rot18():
    rot5 = "5678901234"
    zeroToNine = "0123456789"
    rot_13_key = 5
    msg = demo_var5.msg
    # print("msg can be alphanumeric")
    # msg = input("Enter msg: ").upper()

    decryp_text = ""
    for i in range(len(msg)):
        temp = msg[i] + ""
        if ord(msg[i]) == 32:
            decryp_text += " "
        elif re.search('[\d\s]+', temp):
            # ROT5
            for j in range(len(zeroToNine)):
                if msg[i] == rot5[j]:
                    decryp_text += zeroToNine[j]
                    # inner for
        elif re.search('[\w\s]+', temp):
            # ROT13
            ch_temp = ord(msg[i]) - rot_13_key
            if ord(msg[i]) == 32:
                decryp_text += " "
            elif ch_temp < 65:
                ch_temp += 26
                decryp_text += chr(ch_temp)
            else:
                decryp_text += chr(ch_temp)
                # if-else
    # for

    # print("Decrypted Text: {}".format(decryp_text))
    cipher_decryption_rot18.unread = format(decryp_text)

    # Checking y[1]: index
    if x[1] == "one":
        from one_d import demo_var1, cipher_decryption
        demo_var1()
        demo_var1.msg = cipher_decryption_rot18.unread
        # print(demo_var1.msg)
        cipher_decryption()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption.unrea)

    elif x[1] == "two":
        from two_d import demo_var2, at_decryption
        demo_var2()
        demo_var2.msg = cipher_decryption_rot18.unread
        #    print(demo_var2.msg)
        at_decryption()
        print("Last5 Encrypted form of message pass through different file is:" + at_decryption.message)

    elif x[1] == "three":
        from three_d import demo_var3, cipher_decryption_rail
        demo_var3()
        demo_var3.msg = cipher_decryption_rot18.unread
        #    print(demo_var2.msg)
        cipher_decryption_rail()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_rail.unread)

    elif x[1] == "four":
        from four_d import demo_var4, cipher_decryption_rot47
        demo_var4()
        demo_var4.msg = cipher_decryption_rot18.unread
        #    print(demo_var2.msg)
        cipher_decryption_rot47()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_rot47.unread)

    elif x[1] == "six":
        from six_d import cipher_decryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = cipher_decryption_rot18.unread
        #    print(demo_var2.msg)
        cipher_decryption_xor()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_xor.xorunread)
