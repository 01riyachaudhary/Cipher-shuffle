# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shatter_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Ciphers_enc import *
from Ciphers_dec import *
from random import sample

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 535)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ENCRYPTION = QtWidgets.QPushButton(Dialog)
        self.ENCRYPTION.setGeometry(QtCore.QRect(500, 110, 93, 28))

        self.ENCRYPTION.clicked.connect(self.plain_textBlock)
        self.ENCRYPTION.clicked.connect(self.cipher_task)
        self.ENCRYPTION.clicked.connect(self.cipher_task_dec)
        self.ENCRYPTION.clicked.connect(self.check_if)

        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ENCRYPTION.setFont(font)
        self.ENCRYPTION.setObjectName("ENCRYPTION")

        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.COMMENTBOX = QtWidgets.QLabel(Dialog)
        self.COMMENTBOX.setGeometry(QtCore.QRect(10, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.COMMENTBOX.setFont(font)
        self.COMMENTBOX.setObjectName("COMMENTBOX")
        self.PlainText = QtWidgets.QLineEdit(Dialog)
        self.PlainText.setGeometry(QtCore.QRect(140, 40, 311, 161))
        self.PlainText.setAutoFillBackground(False)
        self.PlainText.setObjectName("PlainText")
        self.TIMEINTERVAL_2 = QtWidgets.QLabel(Dialog)
        self.TIMEINTERVAL_2.setGeometry(QtCore.QRect(10, 420, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TIMEINTERVAL_2.setFont(font)
        self.TIMEINTERVAL_2.setObjectName("TIMEINTERVAL_2")
        self.EncryptedText = QtWidgets.QLineEdit(Dialog)
        self.EncryptedText.setGeometry(QtCore.QRect(140, 210, 311, 161))
        self.EncryptedText.setAutoFillBackground(False)
        self.EncryptedText.setObjectName("EncryptedText")
        self.COMMENTBOX_2 = QtWidgets.QLabel(Dialog)
        self.COMMENTBOX_2.setGeometry(QtCore.QRect(20, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.COMMENTBOX_2.setFont(font)
        self.COMMENTBOX_2.setObjectName("COMMENTBOX_2")
        self.first_index = QtWidgets.QLabel(Dialog)
        self.first_index.setGeometry(QtCore.QRect(100, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_index.setFont(font)
        self.first_index.setObjectName("first_index")
        self.second_index = QtWidgets.QLabel(Dialog)
        self.second_index.setGeometry(QtCore.QRect(170, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_index.setFont(font)
        self.second_index.setObjectName("second_index")
        self.third_index = QtWidgets.QLabel(Dialog)
        self.third_index.setGeometry(QtCore.QRect(250, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.third_index.setFont(font)
        self.third_index.setObjectName("third_index")
        self.fourth_index = QtWidgets.QLabel(Dialog)
        self.fourth_index.setGeometry(QtCore.QRect(320, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fourth_index.setFont(font)
        self.fourth_index.setObjectName("fourth_index")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(410, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ENCRYPTION.setText(_translate("Dialog", "ENCRYPTION"))
        self.COMMENTBOX.setText(_translate("Dialog", "Plain Text"))
        self.TIMEINTERVAL_2.setText(_translate("Dialog", "INDEXES"))
        self.COMMENTBOX_2.setText(_translate("Dialog", "Encrypted Text"))
        self.first_index.setText(_translate("Dialog", "INDEX!"))
        self.second_index.setText(_translate("Dialog", "INDEX!"))
        self.third_index.setText(_translate("Dialog", "INDEX!"))
        self.fourth_index.setText(_translate("Dialog", "INDEX!"))
        self.label_5.setText(_translate("Dialog", "INDEX!"))


    def plain_textBlock(self):
        self.plainText12 = self.PlainText.text()

    def Encrypted_textBlock(self):
        Enc_Text= self.EncryptedText.text()
        #print(Enc_Text)

    def cipher_task(self):
        dict_items = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
        self.crypto_dict = sample(dict_items, 5)

        self.first_index.setText(self.crypto_dict[0])
        self.second_index.setText(self.crypto_dict[1])
        self.third_index.setText(self.crypto_dict[2])
        self.fourth_index.setText(self.crypto_dict[3])
        self.label_5.setText(self.crypto_dict[4])

        crypto_dict_len = len(self.crypto_dict)
        # plain_enc = input("Enter your cipher text Here:")
        plain_enc = self.plainText12
        plainMsg = plain_enc
        self.dock=self.plainText12

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
        self.NativeEnc=plainMsg


    def cipher_task_dec(self):
        dict_arry = self.crypto_dict

        def Reverse(dict_arry):
            new_lst = dict_arry[::-1]
            return new_lst

        self.dict_items = Reverse(dict_arry)
        print(self.dict_items)


        crypto_dict_len = len(self.dict_items)

        plain_dec = self.NativeEnc

        EncryptedMsg = plain_dec

        for i in range(crypto_dict_len):
            if self.dict_items[i] == "one":
                ceaserCipher_decryption(EncryptedMsg)
                EncryptedMsg = ceaserCipher_decryption.plain_dec
            elif self.dict_items[i] == "two":
                atBash_decryption(EncryptedMsg)
                EncryptedMsg = atBash_decryption.plain_dec
            elif self.dict_items[i] == "three":
                railFence_Cipher_decryption(EncryptedMsg)
                EncryptedMsg = railFence_Cipher_decryption.plain_dec
            elif self.dict_items[i] == "four":
                TransportationCipherDec_main(EncryptedMsg)
                EncryptedMsg = TransportationCipherDec_main.plain_dec
            elif self.dict_items[i] == "five":
                XORcipher_decryption(EncryptedMsg)
                EncryptedMsg = XORcipher_decryption.plain_dec
            elif self.dict_items[i] == "six":
                oneTimePad_decryption(EncryptedMsg)
                EncryptedMsg = oneTimePad_decryption.plain_dec
            elif self.dict_items[i] == "seven":
                Autokey_DecryptionMain(EncryptedMsg)
                EncryptedMsg = Autokey_DecryptionMain.plain_dec
            elif self.dict_items[i] == "eight":
                ROT47cipher_decryption(EncryptedMsg)
                EncryptedMsg = ROT47cipher_decryption.plain_dec
        print(EncryptedMsg)
        self.mean=EncryptedMsg

    def check_if(self):
        try:
            if self.mean == self.dock:
                self.EncryptedText.insert(self.NativeEnc)
                print("good")
            else:
                sys.exit()
        except:
            print("ERROR")
            sys.exit()


def main_node():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
main_node()