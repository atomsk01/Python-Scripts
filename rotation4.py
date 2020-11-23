#!/usr/bin/python3

#this is a simple script used to cipher and decipher single words or phrases without spaces

import sys

print("-------------")
print("|Auto-Cipher|")
print("-------------")

#this is the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
#ask the user to cipher or decipher
userMode = (sys.argv[2])
#ask the user for the message
userMessage = (sys.argv[3])
#ask the user for the numerical cipher key
userRotation = (sys.argv[1])
#cipher placeholder that will be accessed during loops
cipher = ""

#encrypt for loop
#if user chooses encrypt, this for loops begins. grabs the letters, converts them one at a time,
#converts to integer for addition
#prints the ciphered message

def enc(x):
    return ((alphabet.index(x) + int(userRotation)) % 26)

def dec(x):
    return ((alphabet.index(x) - int(userRotation)) % 26)

if (userMode == "-e"):
    modeBoi = enc
elif (userMode == "-d"):
    modeBoi = dec
else:
    print("something went wrong. please try the following:")
    print("number of rotations")
    print("encrypt -e")
    print("message")
    print("Example: 3 -e woof")
    exit()

for x in userMessage:
    number = modeBoi(x)
    i = alphabet[number]
    cipher += i
print (f"Your result {cipher}")