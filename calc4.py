#!/usr/bin/python3

#big changes, added argv
#when ./calc4.py to run it, also add the numbers as variables
#example:
# ./calc4.py 12 x 12
# this will then run the program and use 12 as variable x and 12 as variable y
#all you have to do next is answer the first prompt: +, -, /, or x


import sys


print("///CALCU-TRON/// now with argv!")
def addition(x, y):
    answer = x + y
    return answer

def subtraction(x, y):
    answer = x - y
    return answer

def multiplication(x, y):
    answer = x * y
    return answer

def division(x, y):
    answer = x / y
    return answer


x = int(sys.argv[1])
y = int(sys.argv[3])
choice = (sys.argv[2])

if choice == "+":
    answer = addition(x, y) #these call the defined functions using the variables
    print(f"beep beep : your answer is {answer}")
elif choice == "-":
    answer = subtraction(x, y)
    print(f"*robot sounds* : your answer is {answer}")
elif choice == "/":
    answer = division(x, y)
    print(f"whirrr : your answer is {answer}")
elif choice == "x":
    answer = multiplication(x, y)
    print(f"beep-bloop : your answer is {answer}")


