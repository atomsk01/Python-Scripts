#!/usr/bin/python3

#same as login 2, but  user has 5 tries to login.
#make a loop that allows the user to have only 5 chances to login
#create / define  dictionary {}
#ask username
#ask pass
#while loop and counter
#check un and pass against key:value 
#pass print success
#fail print loop x5 then fail


#bit of unecessary flair
print("/// ///// ///// ///// ////// ///")
print("/// Welcome to McDonaldLand! ///")
print("/// ///// ///// ///// ////// ///")

#dictionary
loginDict = {"Grimace" : "duh", "Hamburglar" : "robble!", "MayorMcCheese" : "May0r"} #don't keep these in plain text

#login counter, begin at zero and count up
count = 0

while(True):

#ask un & pass section
    userName = input("/////Please enter your Username: ")
    userPassword = input("/////Please enter your Password: ")

#begin loop stuff
#THE GET COMMAND! its so simple!
#.get is like a two-fer, it checks the dictionary for the variable
#while also matching the username with password *magic*
    if loginDict.get(userName) == userPassword:
#success!
        print("////////////////////////////////")
        print(f"Welcome {userName}, Have you seen Ronald?")
        break #kills instance, but i shouldnt it log in to something?
    else: #begin failure routine
        print("Failed to verify Credentials")
        print("Please try again")
        count += 1 #adds one count each try
        if(count == 5): #when the 0 count reaches 5, it prints fail and terminates
            print("Too many failed attempts")
            print("Terminating connection...")
            exit()

