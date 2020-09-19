#!/usr/bin/python3


#This is a basic password checker implementing a whitelist
#user may only use characters in the whitelist
#getpass is used to hide user input


#this will hide the input as its typed
import getpass
#import this to allow searching of whitelist
import re
#import this to clear screen
import subprocess
subprocess.call('clear', shell=True)


#banner flair
print("------------------------------")
print("| Whitelist Password Checker |")
print("------------------------------")


#colors!
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 


#lists of allowed characters
whitelistupper = "[A-Z]"
whitelistlower = "[a-z]"
whitelistnumbers = "[0-9]"


#begin while loop to check user input against whitelists parameters.
#if fail, print which check failed and re-ask user input
print("Password minimum length of 4 and contain 1 upper, 1 lower, and 1 number.")
#getpass to hide input
password = getpass.getpass("Password: ")
#banana is the counter. if a check fails, -1 and fail. if 0, success
banana = 0


while True:
	if (len(password) < 4): #fail if pass shorter than 4
		banana = -1
		prYellow("Password must be a minimum of 4 characters")
		password = getpass.getpass("Password: ")
	elif not re.search(whitelistupper, password): #fail if not in upper case list
		banana = -1
		prYellow("Password must contain 1 uppercase letter.")
		password = getpass.getpass("Password: ")
	elif not re.search(whitelistlower, password): #fail if not in lower case list
		banana = -1		
		prYellow("Password must contain 1 lowercase letter.") 
		password = getpass.getpass("Password: ")
	elif not re.search(whitelistnumbers, password): #fail if not in number list
		banana = -1
		prYellow("Password must contain 1 number.") 
		password = getpass.getpass("Password: ")
	else:
		banana = 0 #if banana is still 0 after all checks, success! then break
		prGreen("Well done, you've created a valid password.")
		break