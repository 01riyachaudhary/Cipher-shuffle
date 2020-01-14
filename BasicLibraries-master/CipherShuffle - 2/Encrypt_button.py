from Ciphers_enc import *
from Ciphers_dec import *
from random import sample


class Enc_App():
    def cipher_task(self,plain_text):
        dict_items = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
        self.crypto_dict = sample(dict_items, 5)
        print(self.crypto_dict)
        crypto_dict_len = len(self.crypto_dict)
        # plain_enc = input("Enter your cipher text Here:")
        plain_enc = self.plain_text
        plainMsg = plain_enc

        for i in range(crypto_dict_len):
            if self.crypto_dict[i] == "one":
                ceaserCipher_encryption(plainMsg)
                plainMsg = ceaserCipher_encryption.plain_enc
            elif self.crypto_dict[i] == "two":
                atBash_encryption(plainMsg)
                plainMsg = atBash_encryption.plain_enc
            elif self.crypto_dict[i] == "three":
                railFence_Cipher_encryption(plainMsg)
                plainMsg = railFence_Cipher_encryption.plain_enc
            elif self.crypto_dict[i] == "four":
                TransportationCipher_main(plainMsg)
                plainMsg = TransportationCipher_main.plain_enc
            elif self.crypto_dict[i] == "five":
                XORcipher_encryption(plainMsg)
                plainMsg = XORcipher_encryption.plain_enc
            elif self.crypto_dict[i] == "six":
                oneTimePad_encryption(plainMsg)
                plainMsg = oneTimePad_encryption.plain_enc
            elif self.crypto_dict[i] == "seven":
                Autokey_EncryptionMain(plainMsg)
                plainMsg = Autokey_EncryptionMain.plain_enc
            elif self.crypto_dict[i] == "eight":
                ROT47cipher_encryption(plainMsg)
                plainMsg = ROT47cipher_encryption.plain_enc
        print(plainMsg)
        self.NativeEnc=plainMsg




    def cipher_task_dec(self):
        dict_arry = self.crypto_dict

        def Reverse(dict_arry):
            new_lst = dict_arry[::-1]
            return new_lst

        dict_items = Reverse(dict_arry)
        print(dict_items)
        crypto_dict_len = len(dict_items)

        plain_dec = self.NativeEnc
        print(len(plain_dec))

        EncryptedMsg = plain_dec

        for i in range(crypto_dict_len):
            if dict_items[i] == "one":
                ceaserCipher_decryption(EncryptedMsg)
                EncryptedMsg = ceaserCipher_decryption.plain_dec
            elif dict_items[i] == "two":
                atBash_decryption(EncryptedMsg)
                EncryptedMsg = atBash_decryption.plain_dec
            elif dict_items[i] == "three":
                railFence_Cipher_decryption(EncryptedMsg)
                EncryptedMsg = railFence_Cipher_decryption.plain_dec
            elif dict_items[i] == "four":
                TransportationCipherDec_main(EncryptedMsg)
                EncryptedMsg = TransportationCipherDec_main.plain_dec
            elif dict_items[i] == "five":
                XORcipher_decryption(EncryptedMsg)
                EncryptedMsg = XORcipher_decryption.plain_dec
            elif dict_items[i] == "six":
                oneTimePad_decryption(EncryptedMsg)
                EncryptedMsg = oneTimePad_decryption.plain_dec
            elif dict_items[i] == "seven":
                Autokey_DecryptionMain(EncryptedMsg)
                EncryptedMsg = Autokey_DecryptionMain.plain_dec
            elif dict_items[i] == "eight":
                ROT47cipher_decryption(EncryptedMsg)
                EncryptedMsg = ROT47cipher_decryption.plain_dec
        EncryptedMsg == self.mean

        if self.plain_text == self.mean:
            print("SUCESS")
        else:
            print("FAILURE")


if __name__ == '__main__':
    Enc_App()