#!/usr/bin/python3

#1. Walk through this script before you write it and try to guess what is happening.
#2. Now, type it up and see if you were correct.
#3. Next, add 2 more functions: multiplication/division
#4. Lastly, have the user input the two numbers instead of "hard coding" them into your
#script.

#the script first defines some simple math functions instead of importing math.
#then there is a user prompt asking to add or sub
#the script then takes the response and adds or subs the preset variables under def main()

#next step, make it loop!

print("///CALCU-TRON///")
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

def main(): #hard coded variables, we'll fix this below
    x = 2
    y = 4

print("Addition 'add', Subtraction 'sub', Division 'div, or multiplication 'mul'")
print("Please only answer in abbreviated form as stated above")
choice = input("How can Calcu-Tron serve you today? ")
x = int(input("What is the first number? ")) #heres the variable choice
y = int(input("What is the second number? ")) #variable

if choice == "add":
    answer = addition(x, y) #these call the defined functions using the variables
    print(f"beep beep : your answer is {answer}")
elif choice == "sub":
    answer = subtraction(x, y)
    print(f"*robot sounds* : your answer is {answer}")
elif choice == "div":
    answer = division(x, y)
    print(f"whirrr : your answer is {answer}")
elif choice == "mul":
    answer = multiplication(x, y)
    print(f"beep-bloop : your answer is {answer}")
main()
