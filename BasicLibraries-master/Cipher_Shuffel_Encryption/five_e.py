# ROT18 Encryption
import re
from generate_random import y


def demo_var5():
    from random_number import msg
    demo_var5.msg = msg.upper()


def cipher_encryption_rot18():
    rot5 = "5678901234"
    zeroToNine = "0123456789"
    rot_13_key = 5

    # print("msg can be alphanumeric")
    # msg = input("Enter msg: ").upper()
    msg = demo_var5.msg
    encryp_text = ""
    for i in range(len(msg)):
        temp = msg[i] + ""
        if ord(msg[i]) == 32:
            encryp_text += " "
        elif re.search('[\d\s]+', temp):
            # ROT5
            for j in range(len(zeroToNine)):
                if msg[i] == zeroToNine[j]:
                    encryp_text += rot5[j]
            # inner for
        elif re.search('[\w\s]+', temp):
            # ROT13
            ch_temp = ord(msg[i]) + rot_13_key
            if ord(msg[i]) == 32:
                encryp_text += " "
            elif ch_temp > 90:
                ch_temp -= 26
                encryp_text += chr(ch_temp)
            else:
                encryp_text += chr(ch_temp)
        # if-else
    # for

    # print("Encrypted Text: {}".format(encryp_text))
    cipher_encryption_rot18.unread = format(encryp_text)

    # Checking y[1]: index
    if y[1] == "one":
        from one_e import demo_var1, cipher_encryption
        demo_var1()
        demo_var1.msg = cipher_encryption_rot18.unread
        # print(demo_var1.msg)
        cipher_encryption()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_encryption.unrea)
    elif y[1] == "two":
        from two_e import demo_var2, at_encryption
        demo_var2()
        demo_var2.msg = cipher_encryption_rot18.unread
        #    print(demo_var2.msg)
        at_encryption()
        print("Last5 Encrypted form of message pass through different file is:" + at_encryption.message)
    elif y[1] == "three":
        from three_e import demo_var3, cipher_encryption_rail
        demo_var3()
        demo_var3.msg = cipher_encryption_rot18.unread
        #    print(demo_var2.msg)
        cipher_encryption_rail()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_encryption_rail.unread)
    elif y[1] == "four":
        from four_e import demo_var4, cipher_encryption_rot47
        demo_var4()
        demo_var4.msg = cipher_encryption_rot18.unread
        #    print(demo_var2.msg)
        cipher_encryption_rot47()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_encryption_rot47.unread)
    elif y[1] == "six":
        from six_e import cipher_encryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = cipher_encryption_rot18.unread
        # print(demo_var1.msg)
        cipher_encryption_xor()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_xor.xorunread)
