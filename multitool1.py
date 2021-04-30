#!/usr/bin/python3


#ip and port range scanner - defaults or specified by user
#bind shell


#import these things
import subprocess
import socket
import sys
import re
import pty
import os


#this checks for valid IP
def is_valid_ip(ip):
    ipv = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)
    return bool(ipv) and all(map(lambda n: 0<=int(n)<=255, ipv.groups()))


#defines range of IPs
def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []
    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
        ip_range.append(".".join(map(str, temp)))    
    return ip_range


#text COLORS!
subprocess.call('clear', shell=True)
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


#banner flair
prPurple("----------------------")
prPurple("|IP-Socket-Multi-Tool|")
prPurple("----------------------")


#this if statement asks user to check their current localhost IP address
#internet connection not required
#it then uses socket to grab and print it out
userInput = input("Check (i)p address, scan open (p)orts, or (b)ind shell: ")
if userInput == "i":
    userInput2 = input("(l)ocalhost or (r)ange: ")
    if userInput2 == "l":
		#find and print local IP addr + hostname (dont need internet)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        hostname = socket.gethostname()
        print("-" *65)
        prYellow((hostname) + ":   " + s.getsockname()[0])
        print("-" *65)
    if userInput2 == "r":
        uIP1, uIP2 = input("IP range to ping (ex:192.168.0.0-192.168.0.10): ").split("-")
        ip_range = ipRange(uIP1,uIP2)
        print("-" * 65)
        prYellow("IPs responding to pings...")
        for ip in ip_range:
            res = subprocess.call(['ping', '-q', '-c', '1', ip],stdout = subprocess.DEVNULL)
            if res == 0: 
                prPurple(ip)
        print("-" * 65)         


#if the user presses (p) the script moves here
#this asks the user to scan a specific IP for open ports 1-1025
#new addition - user is able to enter custom port range to scan
if userInput == ("p"):


#define true or false variable
	portsFound = False
	invalidIP = True


#ask user for custom or default ip range, also checks for valid IP input
	ui3 = input("(c)ustom range or (d)efault 1-1025: ")
	while invalidIP:
		ipA = input("What is the IP: ")
		if is_valid_ip(ipA):
			invalidIP = False
		else:
			prRed("Invalid IP, shame!")
	ipB = socket.gethostbyname(ipA)


#user choses (c) or (d) move here
#scan default 1-1025 ports or scan range of open ports based on ip given by user
	try:
		if ui3 == "c":
			cr1, cr2 = input("Custom range (xx-xx): ").split("-")
			cr1, cr2 = (int(cr1),int(cr2))
		else:
			cr1 = 1
			cr2 = 1025
		print("-" * 65)
		for port in range(cr1,cr2):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((ipB, port))
			if result == 0:
				prYellow("Port {}:    Open".format(port))
				portsFound = True
	except KeyboardInterrupt:
    		print ("User Terminated")
    		sys.exit()
	if portsFound == False:
		prYellow("No open ports found")
	print("-" * 65)
	sock.close()
	sys.exit()


#user chooses (b) move here
if userInput == ("b"):


#ask if attacker or victim
	userInput = input("(v)ictim or (a)ttacker: ")


# if (v) is chosen - ask for IP & port to listen on
if userInput == ("v"):
    prRed("//Victim Chosen//")
    vIP2 = input("Input IP: ")
    vPort2 = input("Input Port: ")
    BUFFER_SIZE = 1024
    q = socket.socket()
    q.bind((vIP2, int(vPort2)))
    q.listen(10)
    prYellow("Listening...")
    z, y = q.accept()
    prYellow("Connection Established")



#if user chooses (a) move here
if userInput == ("a"):
#will ask for victim IP and port and establish connection for bind shell
#do these things
    prRed("//Attacker Chosen//")
    vIP3 = input("Input IP: ")
    vPort3 = input("Input Port: ")
    BUFFER_SIZE = 1024
    q = socket.socket()
    q.bind((vIP3, int(vPort3)))
    q.listen(10)
    z, y = q.accept()
    prYellow("Connection Established")
