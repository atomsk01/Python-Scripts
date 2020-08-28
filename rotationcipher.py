#!/usr/bin/python3

#this is a simple script used to cipher and decipher single words or phrases without spaces

print("-------------")
print("|Auto-Cipher|")
print("-------------")

#this is the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
#ask the user to cipher or decipher
userMode = input("would you like to encrypt or decrypt? ('e' or 'd') ")
#ask the user for the message
userMessage = input("What is the message? ")
#ask the user for the numerical cipher key
userRotation = input("What is the key? (Numbers only) ")
#cipher placeholder that will be accessed during loops
cipher = ""

#encrypt for loop
#if user chooses encrypt, this for loops begins. grabs the letters, converts them one at a time,
#converts to integer for addition
#prints the ciphered message
if (userMode == "e"):
    for x in userMessage:
        number = ((alphabet.index(x) + int(userRotation)) % 26)
        i = alphabet[number]
        cipher += i
    print (f"Your cipher is {cipher}")

#decrypt for loop
#same as encryption code above but subtracts instead of adds
if (userMode == "d"):
    for x in userMessage:
        number = ((alphabet.index(x) - int(userRotation)) % 26)
        i = alphabet[number]
        cipher += i
    print (f"The answer is probably {cipher}.")


