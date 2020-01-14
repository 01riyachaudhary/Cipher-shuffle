import onetimepad

msg=input("Enter Your Text: ")
cipher = onetimepad.encrypt(msg,  'keypathhere')
print("Encrypted Message is :",cipher)
