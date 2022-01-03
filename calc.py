import os
from colorama import Fore
def add(num1, num2):
    try:
        add.output = float(num1) + float(num2)
    except: print("Could not complete operation.")

def div(num1, num2):
    try:
        div.output = float(num1) / float(num2)
    except: print("Could not complete operation.")

def mul(num1, num2):
    try:
        mul.output = float(num1) * float(num2)
    except: print("Could not complete operation.")

def sub(num1, num2):
    try:
        sub.output = float(num1) - float(num2)
    except: print("Could not complete operation.")
    
mem = 0
float(mem)
run = True
os.system('clear')
print("Computey calc 1.0 By Jack Yellow")
while run == True:

    calcin = input("Would you like to (A)dd, (S)ubtract, (M)ultiply, (D)ivide, (H)elp, (C)opy last output to memory, c(L)ear screen or (E)xit?")
    if calcin == "a":
        num1 = input("Enter first number to add. ")
        num2 = input("Enter second number to add. ")
        if num1 == "mem":
            num1 = mem
        if num2 == "mem":
            num2 = mem
        add(num1, num2)
        print(add.output)
        out = add.output
    if calcin == "s":
        num1 = input("Enter first number to subtract. ")
        num2 = input("Enter second number to subtract. ")
        if num1 == "mem":
            num1 = mem
        if num2 == "mem":
            num2 = mem
        sub(num1, num2)
        print(sub.output)
        out = sub.output
    if calcin == "m":
        num1 = input("Enter first number to multiply. ")
        num2 = input("Enter second number to multiply. ")
        if num1 == "mem":
            num1 = mem
        if num2 == "mem":
            num2 = mem
        mul(num1, num2)
        print(mul.output)
        out = mul.output
    if calcin == "d":
        num1 = input("Enter first number to divide. ")
        num2 = input("Enter second number to divide. ")
        if num1 == "mem":
            num1 = mem
        if num2 == "mem":
            num2 = mem
        div(num1, num2)
        print(div.output)
        out = div.output
    if calcin == "c":
        try:
            mem = out
            print("Saved to memory. Value: " + str(mem))
        except: print("Couldn't save to memory.")
    if calcin == "l":
        os.system("clear")
    if calcin == "h":
        print(Fore.BLUE +  """Welcome to computey calc! This is a calculator application for the computey system. Here are all the commands explained:""" + Fore.WHITE +
                 """
                 a: Adds two numbers together.
                 s: Subtracts two numbers.
                 m: multiplies two numbers.
                 d: divides two numbers.
                 c: copies the the number that was just outputted into memory.
                 if you'd like to use the number in a calculation, type "mem" into the input field. 
                 h: displays this message.
                 l: clears display.
                 e: exits calc.
                 """)
    if calcin == "e":
        os.system("clear")
        run = False
