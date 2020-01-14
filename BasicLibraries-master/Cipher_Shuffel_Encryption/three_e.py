# rail fence Encrytion
import re
from generate_random import y


def demo_var3():
    from random_number import msg
    demo_var3.msg = msg


def cipher_encryption_rail():
    # msg = input("Enter message: ")
    rails = 3
    msg = demo_var3.msg
    # removing white space from message
    msg = msg.replace(" ", "")
    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('.')
        # inner for
    # for

    # testing the matrix
    # for row in railMatrix:
    #     for column in row:
    #         print(column, end="")
    #     print("\n")
    #     # inner for
    # # for

    # putting letters of message one by one in the matrix in zig-zag
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else

    # testing the matrix with message in zig-zag
    # for row in railMatrix:
    #     for column in row:
    #         print(column, end="")
    #     print("\n")
    #     # inner for
    # # for

    encryp_text = ""
    for i in range(rails):
        for j in range(len(msg)):
            encryp_text += railMatrix[i][j]
    # for

    # removing '.' from encrypted text
    encryp_text = re.sub(r"\.", "", encryp_text)
    # print("Encrypted Text: {}".format(encryp_text))
    cipher_encryption_rail.unread = format(encryp_text)

    # Checking y[1]: index

    if y[1] == "one":
        from one_e import demo_var1, cipher_encryption
        demo_var1()
        demo_var1.msg = cipher_encryption_rail.unread
        # print(demo_var1.msg)
        cipher_encryption()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_encryption.unrea)
    elif y[1] == "two":
        from two_e import demo_var2, at_encryption
        demo_var2()
        demo_var2.msg = cipher_encryption_rail.unread
        #    print(demo_var2.msg)
        at_encryption()
        print("Last2 Encrypted form of message pass through different file is:" + at_encryption.message)
    elif y[1] == "four":
        from four_e import demo_var4, cipher_encryption_rot47
        demo_var4()
        demo_var4.msg = cipher_encryption_rail.unread
        #    print(demo_var2.msg)
        cipher_encryption_rot47()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_encryption_rot47.unread)
    elif y[1] == "five":
        from five_e import demo_var5, cipher_encryption_rot18
        demo_var5()
        demo_var5.msg = cipher_encryption_rail.unread
        # print(demo_var1.msg)
        cipher_encryption_rot18()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_encryption_rot18.unread)
    elif y[1] == "six":
        from six_e import cipher_encryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = cipher_encryption_rail.unread
        # print(demo_var1.msg)
        cipher_encryption_xor()
        print("Last1 Encrypted form of message pass through different file is:" + cipher_encryption_xor.xorunread)
