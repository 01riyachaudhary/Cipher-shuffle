# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decr_shatter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Ciphers_dec import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 249)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 40, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 40, 51, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 40, 51, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(230, 40, 51, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(290, 40, 51, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.Encrypted = QtWidgets.QTextEdit(Dialog)
        self.Encrypted.setGeometry(QtCore.QRect(20, 90, 221, 61))
        self.Encrypted.setObjectName("Encrypted")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 170, 221, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 61, 16))
        self.label_3.setObjectName("label_3")
        self.Dec_button = QtWidgets.QPushButton(Dialog)
        self.Dec_button.setGeometry(QtCore.QRect(260, 140, 101, 41))
        self.Dec_button.setObjectName("Dec_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Dec_button.clicked.connect(self.get_encText)
        self.Dec_button.clicked.connect(self.get_index)
        self.Dec_button.clicked.connect(self.cipher_task_dec)

    def get_encText(self):
        self.get_varencText = self.Encrypted.toPlainText()

    def get_index(self):
        self.first_index = self.comboBox.currentText()
        self.second_index = self.comboBox_2.currentText()
        self.third_index = self.comboBox_3.currentText()
        self.fourth_index = self.comboBox_4.currentText()
        self.fifth_index = self.comboBox_5.currentText()

        #self.reverse_index = "[" +"'" +self.first_index+ "'" + "," + "'" +self.second_index+"'"  + "," + "'" +self.third_index+"'"  + "," + "'" +self.fourth_index+"'"  + "," + "'" +self.fifth_index+"'" +  "]"
        #print(self.reverse_index)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "INDEX"))
        self.comboBox.setItemText(0, _translate("Dialog", "one"))
        self.comboBox.setItemText(1, _translate("Dialog", "two"))
        self.comboBox.setItemText(2, _translate("Dialog", "three"))
        self.comboBox.setItemText(3, _translate("Dialog", "four"))
        self.comboBox.setItemText(4, _translate("Dialog", "five"))
        self.comboBox.setItemText(5, _translate("Dialog", "six"))
        self.comboBox.setItemText(6, _translate("Dialog", "seven"))
        self.comboBox.setItemText(7, _translate("Dialog", "eight"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "one"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "two"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "three"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "four"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "five"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "six"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "seven"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "eight"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "one"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "two"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "three"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "four"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "five"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "six"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "seven"))
        self.comboBox_3.setItemText(7, _translate("Dialog", "eight"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "one"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "two"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "three"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "four"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "five"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "six"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "seven"))
        self.comboBox_4.setItemText(7, _translate("Dialog", "eight"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "one"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "two"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "three"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "four"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "five"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "six"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "seven"))
        self.comboBox_5.setItemText(7, _translate("Dialog", "eight"))
        self.label_2.setText(_translate("Dialog", "Encrypted Text"))
        self.label_3.setText(_translate("Dialog", "Plain Text"))
        self.Dec_button.setText(_translate("Dialog", "DECRYPT"))

    def cipher_task_dec(self):

        dict_arry =[self.first_index,self.second_index,self.third_index,self.fourth_index,self.fifth_index]


        def Reverse(dict_arry):
            new_lst = dict_arry[::-1]
            return new_lst

        dict_items = Reverse(dict_arry)
        print(dict_items)
        print(type(dict_items))
        crypto_dict_len = len(dict_items)

        plain_dec = self.get_varencText
        print(len(plain_dec))
        print(type(dict_items[0]))
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
        self.textEdit_2.setText(EncryptedMsg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

