import time
import os
import platform
import sys

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def man():
    bold = '\033[1m'
    dim = '\033[2m'
    yellow = '\033[33m'
    reset = '\033[0m'
    
    clear_screen()

    print(f"{yellow}{bold}Hello World, I Made a Calculator! 🎉{reset}\n")
    
    print(f"""Welcome to {yellow}{bold}Calculatore{reset} a simple command-line calculator with a unique feature: it understands words as operators. This is my first program and started as a fun experiment to see if I could build a calculator.\n""")

    print(f"### {bold}How It Works{reset}\n")
    
    print(f"Calculatore performs arithmetic operations using either symbols or words. After each calculation, the result will be used as the starting point for the next calculation unless you type {yellow}{bold}\"reset\"{reset}.\n")
    
    print(f"### {bold}Examples{reset}\n")
    print(f"- {yellow}1 plus 3.5{reset}\n  Adds 3.5 to 1, resulting in 4.5.\n")
    print(f"- {yellow}divided by 6{reset}\n  Divides the previous result (4.5) by 6, resulting in 0.75.\n")
    
    print(f"### {bold}Supported Operators{reset}\n")
    print(f"You can use the following operators:\n")
    print(f"- {yellow}{bold}Addition{reset}: {yellow}plus{reset} or {yellow}+{reset}")
    print(f"- {yellow}{bold}Subtraction{reset}: {yellow}minus{reset} or {yellow}-{reset}")
    print(f"- {yellow}{bold}Division{reset}: {yellow}divided by{reset} or {yellow}/{reset}")    
    print(f"- {yellow}{bold}Multiplication{reset}: {yellow}times{reset} or {yellow}*{reset}\n")
    
    print(f"### {bold}Additional Commands{reset}\n")
    print(f"- {yellow}\"reset\"{reset}: Resets the calculator to start fresh.")
    print(f"- {yellow}CTRL + C{reset}: Exits the program.\n")
    
    print(f"### {bold}Usage{reset}\n")
    print(f"Just enter your calculations directly in the terminal!\n")
    print(f"For example:\n")
    print(f"- {yellow}1 plus 3.5{reset}")
    print(f"- {yellow}divided by 6{reset}")
    print(f"- {yellow}reset{reset}\n")
    
    print(f"### {bold}Contact{reset}\n")
    print(f"Developer: {yellow}Dorian B.{reset}")
    print(f"E-mail: {yellow}doribenbass@gmail.com{reset}")
    print(f"Website: {yellow}doribenba.framer.website{reset}")
    print(f"GitHub Repo: {yellow}https://github.com/doribenba/calculatore{reset}\n")
    

    sys.exit()
    

def calcul():
    print("""\033[4m\033[1mCalculatore
\033[0m""")
    print("""A simple command- line calculator""")
    print('\033[2mType "man" for Manual\033[0m')
    print("")
    print("\033[33m\033[5m= \033[0m", end='')
    operation = input('')
    operation = operation.replace('divided by', '/')
    operation = operation.replace('times', '*')
    operation = operation.replace('plus', '+')
    operation = operation.replace('minus', '-')
    if operation == 'reset':
        clear_screen()
        calcul()
    elif operation == 'man':
        man()
    else:
        try:
            global result
            result = eval(operation)
            print('\033[33m\033[5m= \033[0m\033[33m' + str(result) + '\033[0m', end='')
            if result is not None:
                calcul2(result)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError, ValueError, OverflowError, FloatingPointError) as e:
            print(f"\033[31mError: {e}\033[0m")
            time.sleep(1)
            clear_screen()
            calcul()
        
def calcul2(result):
    while True:
        operation = input(" ")
        operation = operation.lower()  # Convert to lowercase
        operation = operation.replace("divided by", "/")
        operation = operation.replace("times", "*")
        operation = operation.replace("plus", "+")
        operation = operation.replace("minus", "-")
        operation = operation.strip()
        if operation == 'reset':
            clear_screen()
            calcul()
        elif operation == 'man':
            man()
        else:
            try:
                result = eval(f"{result}{operation}")
                print('\033[33m\033[5m= \033[0m\033[33m' + str(result) + '\033[0m', end='')
            except (SyntaxError, NameError, TypeError, ZeroDivisionError, ValueError, OverflowError, FloatingPointError) as e:
                print(f"\033[31mError: {e}\033[0m")
                time.sleep(1)
                clear_screen()
                calcul()
        
try:   
    clear_screen()  
    calcul()
except KeyboardInterrupt:
    sys.exit()
