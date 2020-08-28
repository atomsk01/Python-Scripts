#!/usr/bin/python3

#Let's build a calculator!
#The first line is printing out Basic Calculator 2
#next its defining what x and y are.
#now the script is prompting the user addition or subraction
#if the user chooses add, it adds x and y and returns the answer
#otherwise, it choses subtraction and subtracts them for you and prints the answer

#now let's build and test it
print("Basic Calculator 2")
x = 2 #change this to variable
y = 4 #change this to variable
choice = input("Addition, Subtraction, Division, or Multiplication? ('add, 'sub', 'div', 'mul')?")
var1 = int(input("What is the first number? ")) #heres the variables!
var2 = int(input("What is the second number? ")) #step 5
if choice == "add":
    print("You chose addition")
    print("Your answer is:" ,var1+var2)
#step3, add 3 elif statements for:
#subtraction/multiplication/division
elif choice == "sub": #elif is else if, moves along, checking each for what the user typed
    print("You chose subtraction")
    print("Your answer is:", var1-var2)
elif choice == "mul":
    print("You chose multiplication")
    print("Your answer is:", var1*var2)
elif choice  == "div":
    print("You chose division")
    print("Your answer is:", var1/var2)
else: #step 4
    print("Please only type 'add', 'sub', 'mul', 'div'") 

