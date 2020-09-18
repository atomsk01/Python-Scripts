#! python3

#find what hour it currently is
#find what day of the week it currently is
#run the correct VM for that day + time

#we need modules datetime, calendar, & time
#subprocess to open and run vboxmanager and the vm
from datetime import date
import calendar, time, subprocess

#variables! 
#dothething grabs the vboxmanage path
#runvm<name> specifies which vm to run and how to run it
dothething = "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
runvmNET = (dothething, "startvm", "Ubuntu 18.04 Clone NET")
runvmSYS = (dothething, "startvm", "Ubuntu 18.04 Clone SYS")
runvmCRYPT = (dothething, "startvm", "Ubuntu 18.04 Clone new CRYPT")

#sets up for the current date and time
def dh(): #for 'd'ate and 'h'our
    my_date = date.today()
    today = calendar.day_name[my_date.weekday()]
    hour = time.strftime("%H")
    return today,hour

#this sets up which vm will be run based on day and time 
#if before 12 or after 12 on each specific day
def vbox(dh):
    if dh[0] == 'Monday' and int(dh[1])< 12:
        print("Monday morning, opening NET VM")
        subprocess.Popen(runvmNET)
    elif dh[0] == 'Monday' and int(dh[1])> 12:
        print("Monday afternoon, opening SYS VM")
        subprocess.Popen(runvmSYS)       
    elif dh[0] == 'Tuesday' and int(dh[1])< 12:
        print("Tuesday morning, starting CRYPT VM")
        subprocess.Popen(runvmCRYPT)
    elif dh[0] == 'Tuesday' and int(dh[1])> 12:
        print("Tuesday afternoon, enjoy Strategy. No VM to open")
    elif dh[0] == 'Wednesday' and int(dh[1])< 12:
        print("Wednesday morning, starting NET VM")
        subprocess.Popen(runvmNET)
    elif dh[0] == 'Wednesday' and int(dh[1])> 12:
        print("Wednesday afternoon, opening SYS VM")
        subprocess.Popen(runvmSYS)
    elif dh[0] == 'Thursday' and int(dh[1])< 12:
        print("Thursday morning, starting CRYPT VM")
        subprocess.Popen(runvmCRYPT)
    elif dh[0] == 'Thursday' and int(dh[1])> 12:
        print("Tuesday afternoon, enjoy Strategy. No VM to open")    
    elif dh[0] == 'Friday' and int(dh[1])< 12:
        print("Friday morning, starting NET VM")
        subprocess.Popen(runvmNET)
    elif dh[0] == 'Friday' and int(dh[1])> 12:
        print("Friday afternoon, starting SYS VM")
        subprocess.Popen(runvmSYS)


if __name__ == "__main__":
    vbox(dh())
