# ceaser Encryption
from generate_random import y


def demo_var1():
    from random_number import msg
    demo_var1.msg = msg


def cipher_encryption():
    key = "5"
    msg = demo_var1.msg
    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    # print("Encrypted Text: {}".format(encrypt_hex))
    cipher_encryption.unrea = format(encrypt_hex)

    # Checking y[1]: index

    if y[1] == "two":
        from two_e import demo_var2, at_encryption
        demo_var2()
        demo_var2.msg = cipher_encryption.unrea
        # print(demo_var2.msg)
        at_encryption()
        print("Last7 Encrypted form of message pass through different file is:" + at_encryption.message)
    elif y[1] == "three":
        from three_e import demo_var3, cipher_encryption_rail
        demo_var3()
        demo_var3.msg = cipher_encryption.unrea
        #    print(demo_var2.msg)
        cipher_encryption_rail()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_rail.unread)
    elif y[1] == "four":
        from four_e import demo_var4, cipher_encryption_rot47
        demo_var4()
        demo_var4.msg = cipher_encryption.unrea
        #    print(demo_var2.msg)
        cipher_encryption_rot47()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_rot47.unread)
    elif y[1] == "five":
        from five_e import demo_var5, cipher_encryption_rot18
        demo_var5()
        demo_var5.msg = cipher_encryption.unrea
        # print(demo_var1.msg)
        cipher_encryption_rot18()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_rot18.unread)
    elif y[1] == "six":
        from six_e import cipher_encryption_xor,demo_var6
        demo_var6()
        demo_var6.msg = cipher_encryption.unrea
        # print(demo_var1.msg)
        cipher_encryption_xor()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_xor.xorunread)
