import onetimepad

msg=input("Enter Your Text: ")
dec_msg = onetimepad.decrypt(msg, 'keypathhere')
print("Decrypted Message is: ",dec_msg)