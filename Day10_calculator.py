def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Adding functions to dictionary as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calculator():
    should_accumulate = True
    first_number = float(input("What's your first number?: " ))

    while should_accumulate:
        # dictionary operations to perform calculations.
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operator: ")
        second_number = float(input("What's your next number?: "))
        result = operations[operation_symbol](first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {result}")

        choice = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.")

        if choice == 'y':
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # recursion 

calculator()