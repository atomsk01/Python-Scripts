#!/usr/bin/python3

#another login script
#prompt the user for a username & password
#create a dictionary that has 3 different "key:value" pairs
#using one or more conditional statements, check if the key matches
#make a loop that allows 5 chances
#import module getpass and have it hide the user input password

#do what it says above, but lets do the import and dict first

#lets research this
import getpass


#dictionary key:value
loginDict={"Scooby":"Doo", "Scrappy":"Doo", "Shaggy":"ZOINKS!"}


#start at 0 and work up to 5
count=0

#begin while loop
while(True):

#unecessary flair
    print("??????????????????????????????????????????????????")
    print("Welcome to the Mystery Machine Auto Pilot Console!")
    print("??????????????????????????????????????????????????")
#begin asking for user input here
    userName = input("What is your name? ")
#   userPass = input("What is your password? ")
#So we're using getpass to hide the userPass here
    userPass = getpass.getpass("What is your password? ")
#if statements to check user input with dictionary key:value
    if loginDict.get(userName) == userPass:
        print(f"Welcome {userName}, good luck solving that mystery!")
        break
    else: #begin failure code
        print("Jinkies! You typed something wrong, try again...")
        count += 1 #cout from 0 up to 5
        if(count == 5): # caps the loop at 5 tries
            print("Too many tries!")
            print("No Scooby Snacks for you!")
            exit()
