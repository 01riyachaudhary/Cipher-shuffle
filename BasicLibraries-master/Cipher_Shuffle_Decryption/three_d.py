# rail fence
import re
from Decryption import x


def demo_var3():
    from Decryption import msg
    demo_var3.msg = msg


def cipher_decryption_rail():
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

    # reordering the matrix
    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                # skipping '.'
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1
            # if-else
        # inner for
    # for

    # testing matrix reorder
    for i in railMatrix:
        for column in i:
            print(column, end="")
        # inner for
        print("\n")
    # for

    # putting reordered matrix into decrypted text string to get decrypted text
    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(msg)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else
    # for

    decryp_text = re.sub(r"\.", "", decryp_text)
    # print("Decrypted Text: {}".format(decryp_text))
    cipher_decryption_rail.unread = format(decryp_text)

    # Checking y[1]: index

    if x[1] == "one":
        from one_d import demo_var1, cipher_decryption
        demo_var1()
        demo_var1.msg = cipher_decryption_rail.unread
        # print(demo_var1.msg)
        cipher_decryption()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_decryption.unrea)

    elif x[1] == "two":
        from two_d import demo_var2, at_decryption
        demo_var2()
        demo_var2.msg = cipher_decryption_rail.unread
        #    print(demo_var2.msg)
        at_decryption()
        print("Last2 Encrypted form of message pass through different file is:" + at_decryption.message)

    elif x[1] == "four":
        from four_d import demo_var4, cipher_decryption_rot47
        demo_var4()
        demo_var4.msg = cipher_decryption_rail.unread
        #    print(demo_var2.msg)
        cipher_decryption_rot47()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_decryption_rot47.unread)

    elif x[1] == "five":
        from five_d import demo_var5, cipher_decryption_rot18
        demo_var5()
        demo_var5.msg = cipher_decryption_rail.unread
        # print(demo_var1.msg)
        cipher_decryption_rot18()
        print("Last3 Encrypted form of message pass through different file is:" + cipher_decryption_rot18.unread)

    elif x[1] == "six":
        from six_d import cipher_decryption_xor, demo_var6
        demo_var6()
        demo_var6.msg = cipher_decryption_rail.unread
        #    print(demo_var2.msg)
        cipher_decryption_xor()
        print("Last5 Encrypted form of message pass through different file is:" + cipher_decryption_xor.xorunread)
