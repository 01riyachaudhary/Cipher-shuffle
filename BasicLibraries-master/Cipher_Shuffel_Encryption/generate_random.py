from random import *

# , three, four, five
one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
items = [one, two, three, four, five, six]
# x = sample(items, 1)
#y = sample(items, 2)
y = ['five','three']

if y == ['four', 'two'] :
    y = ['two', 'four']
if y == ['four', 'five'] or y == ['one', 'five'] or y == ['three', 'five']:
    y = ['five','three']
if  y == ['six','two']:
    y = ['two', 'six']
print("Sorry for Inconvenience .")
print("Because you can not enter any symbols and any space in plain text.")
print("and also the decryption is always shown in uppercase")
message = input("Enter your Plain Text to encrypt: ").upper()
#message = input("Enter your Plain Text to encrypt: ").upper()
print(y)
