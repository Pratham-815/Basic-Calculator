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


n1 = int(input("Enter the first number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the above options: ")

n2 = int(input("Enter the second number: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(n1, n2)

print(f"{n1} {operation_symbol} {n2} = {answer}")




