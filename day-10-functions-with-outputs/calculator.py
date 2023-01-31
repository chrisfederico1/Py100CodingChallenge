# Calculator

# import Art
from art import logo


# Adding function
def add(n1, n2):
    return n1 + n2


# Subtracting function
def subtract(n1, n2):
    return n1 - n2


# Multiplication Function
def multiply(n1, n2):
    return n1 * n2


# Division Function
def divide(n1, n2):
    return n1 / n2

# Create a dictionary called operations where keys are +-*/ and the values 
# are the names of the function
operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
}


def calculator():

    # print Art
    print(logo)

    num1 = (float(input("What is the first number?: ")))

    for item in operations:
        print(item)

    flag = "True"


    while flag == "True":
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = (float(input("What is the next number?: ")))
        # create a variable that calls the operations dictionary and matches the
        # symbol
        # This will then call the function stored in the dictionary
        calculation_function = operations[operation_symbol]

        # next create a variable that uses that calculation function to pass in the
        # numbers
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        check_user = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if check_user == "n":
            flag = "False"
            calculator()
        else:
            num1 = answer


calculator()
