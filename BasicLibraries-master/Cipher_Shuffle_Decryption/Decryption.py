import sys
from get_decrypted_msg_and_index import message, index
sys.setrecursionlimit(100000)
check_var = ""
sec_msg = ""
x = index
msg = message
if __name__ == "__main__":
    while True:
        if x[0] == "one":
            from one_d import cipher_decryption, demo_var1
            demo_var1()
            cipher_decryption()
            exit()
        elif x[0] == "two":
            from two_d import at_decryption, demo_var2
            demo_var2()
            at_decryption()
            exit()
        elif x[0] == "three":
            from three_d import cipher_decryption_rail, demo_var3
            demo_var3()
            cipher_decryption_rail()
            exit()
        elif x[0] == "four":
            from four_d import cipher_decryption_rot47, demo_var4
            demo_var4()
            cipher_decryption_rot47()
            exit()
        elif x[0] == "five":
            from five_d import cipher_decryption_rot18, demo_var5
            demo_var5()
            cipher_decryption_rot18()
            exit()
        elif x[0] == "six":
            from six_d import cipher_decryption_xor, demo_var6
            demo_var6()
            cipher_decryption_xor()
            exit()

