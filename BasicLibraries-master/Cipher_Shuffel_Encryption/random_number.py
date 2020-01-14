import time
import sys
from generate_random import message
start_time = time.time()
sys.setrecursionlimit(100000)

# msg = "message"
# msg = "6d0067670c0600"
# message = input("Enter message: ")

check_var = ""
sec_msg = ""
msg = message

if __name__ == "__main__":
    while True:
        from generate_random import y
        if y[0] == "one":
            from one_e import cipher_encryption, demo_var1
            demo_var1()
            cipher_encryption()
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

        elif y[0] == "two":
            from two_e import at_encryption, demo_var2
            demo_var2()
            at_encryption()
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

        elif y[0] == "three":
            from three_e import cipher_encryption_rail, demo_var3
            demo_var3()
            cipher_encryption_rail()
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

        elif y[0] == "four":
            from four_e import cipher_encryption_rot47, demo_var4
            demo_var4()
            cipher_encryption_rot47()
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

        elif y[0] == "five":
            from five_e import cipher_encryption_rot18, demo_var5
            demo_var5()
            cipher_encryption_rot18()
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

        elif y[0] == "six":
            from six_e import cipher_encryption_xor,demo_var6
            demo_var6()
            cipher_encryption_xor()
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

