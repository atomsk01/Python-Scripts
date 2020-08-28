#!/usr/bin/python3

#Slide notes:
#This is a Two Dimensional List
#Things to note:
#1. List of Lists
#2. Nested "for" loop
#Assignment Details:
#test it
#try to figure out what it does and why/how it does it.
#what is the purpose of the two "for" loops?
#submit a paragraph about what you think the script does

list0 = []
list1 = []
list2 = []

table = [list0, list1, list2]

count = 0
for t in table: #the t is the temp variable that goes through the table
    for i in range(4): #this is the count that tells to stop at 4 before breaking
        t.append(str((count * 4) + i + 1)) #append adds to the end of the list
    print(" ".join(t)) #so the " " is a space and the .join command literally joins the numbers together
    count +=1 #its going to add 1 each count

#running the code provides the results:
#1 2 3 4 
#5 6 7 8 
#9 10 11 12

#The script is counting by 1s, starting at 1, and returning after every 4 numbers.
#We have three lists and the temp variable t is looped through each list, gaining 1 number
#each time from the count += command.
#the .join line "joins" the numbers together with a space between each.
#So, we add on to list0 1 2 3 4, then t moves to list1 and 5 6 7 8, then list2 and 
#9, 10, 11, 12. There are three lists and 4 numbers each list and that is what stops
#the for loop.
