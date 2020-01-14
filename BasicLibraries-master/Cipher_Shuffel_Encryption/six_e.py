# XOR encryption
from generate_random import y


def demo_var6():
    from random_number import msg
    demo_var6.msg = msg

def cipher_encryption_xor():
    #msg = input("Enter message: ")
    msg = demo_var6.msg
    key = "5"

    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0

    # print("Encrypted Text: {}".format(encrypt_hex))
    cipher_encryption_xor.xorunread = format(encrypt_hex)

    # Checking y[1]: index
    if y[1] == "one":
        from one_e import demo_var1, cipher_encryption
        demo_var1()
        demo_var1.msg = cipher_encryption_xor.xorunread
        # print(demo_var1.msg)
        cipher_encryption()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_encryption.unrea)
    elif y[1] == "two":
        from two_e import demo_var2, at_encryption
        demo_var2()
        demo_var2.msg = cipher_encryption_xor.xorunread
        #    print(demo_var2.msg)
        at_encryption()
        print("Last5 Encrypted form of message pass through different file is:" + at_encryption.message)
    elif y[1] == "three":
        from three_e import demo_var3, cipher_encryption_rail
        demo_var3()
        demo_var3.msg = cipher_encryption_xor.xorunread
        #    print(demo_var2.msg)
        cipher_encryption_rail()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_encryption_rail.unread)
    elif y[1] == "four":
        from four_e import demo_var4, cipher_encryption_rot47
        demo_var4()
        demo_var4.msg = cipher_encryption_xor.xorunread
        #    print(demo_var2.msg)
        cipher_encryption_rot47()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_encryption_rot47.unread)
    elif y[1] == "five":
        from five_e import demo_var5, cipher_encryption_rot18
        demo_var5()
        demo_var5.msg = cipher_encryption_xor.xorunread
        # print(demo_var1.msg)
        cipher_encryption_rot18()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_encryption_rot18.unread)


