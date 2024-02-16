import os

from art import logo


def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def remainder(n1, n2):
    return n1%n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide 
}

def calculator():

    print(logo)

    is_on = True

    n1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the above options: ")

    n2 = float(input("Enter the second number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {answer}")

    while is_on:
        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit, or type 'z' to start new calculation: ")

        if choice=='n':
            is_on = False
            print(f"Exiting the calculator!!!...\n")
        
        elif choice=='y':
            n3 = float(input("Enter the next number: "))
            operation_symbol = input("Pick an operation: ")
            calculation_function = operations[operation_symbol]
            answer2 = calculation_function(answer, n3)
            print(f"{answer} {operation_symbol} {n3} = {answer2}")

        else:
            is_on = False
            os.system('cls')
            calculator()


calculator()
