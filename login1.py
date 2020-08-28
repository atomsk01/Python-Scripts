#!/usr/bin/python3

#ask for username & password
#create lists ulist & plist
#Username:
#Password:
#return <Logging in> or <Failed to login>
#if username = ulist, ask for password, else fail
#if password = plist, return "logging in"

#username list
ulist = ["Captain Planet"]

#password list (shouldn't this be encrypted?)
plist = ["THE POWER IS YOURS!!"]

print("||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||")
print("|||||Welcome Planeteers|||||||")
print("||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||")

#ask username section
userInput = input("What is your Username?: ")
if (ulist[0] == userInput): #[0]not sure how to change this to allow more users
    print("Retinal Scan... Don't move...") #not sure how else to move the script along
else: #This is the fail response
    print("Failed to verify credentials.")
    print("Stop Polluting our servers!")
    print("Connection Terminated...")
    exit() #This kills the script after it fails

#ask password section
userPassword = input("Please verify your password: ")
if (plist[0] == userPassword): #same as ulist[0] this needs to be fixed
    print("|||||||||||Earth!|||||||||||")
    print("|||||||||||Fire!||||||||||||")
    print("|||||||||||Wind!||||||||||||") 
    print("|||||||||||Water!|||||||||||")
    print("|||||||||||Heart!|||||||||||")
    print("||||||||||||||||||||||||||||")
    print("With your powers combined...")
    print("   I am Captain Planet!     ")
    print("||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||")
else:
    print("Failed to verify credentials...")
    print("Nice try, Looten Plunder, Captain Planet is coming for you!")
    print("GO PLANET!")

