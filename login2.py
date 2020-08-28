#!/usr/bin/python3

#same as login 1, but  user has 5 tries to login.
#using a nested if statement, check if the username & password are in the "ulist" and "plist" lists
#make a loop that allows the user to have only 5 chances to login

#create both lists
#ask username
#ask password
#username list
#create loop, check input with lists
#if un and pass match - pass
#if un and pass dont match - fail and loop back 5 times then fail

ulist = ["Mickey Mouse", "Donald Duck"] #Mickey is admin, obvi

#password list (shouldn't this be encrypted?)
plist = ["klubz r kewl!@", "DuckS0undz"]

#hopefully this works for while statement
count  = 0

#I got this from the class slides and I understand how True works,
#I'm just not entirely certain how it know what i'm talking about
while(True):

#ask un & pass section
    userName = input("What is your Username?: ")
    userPassword = input("What is your Password?: ")

#begin loop stuff
    if userName in ulist: #first time ive used it like this, should smooth out login1.py
        if userPassword in plist: #but I guess thats what you meant by "nested"
            print("Welcome to the Mickey Mouse Club!") #success!
            break #kills instance
    else:
        print("Failed to verify Credentials")
        print("Please try again")
        count += 1 #adds one count each try
        if(count == 5): #when the 0 count reaches 5, it prints fail and terminates
            print("Too many failed attempts")
            print("Terminating connection...")
            exit()
