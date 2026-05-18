# Day 5: Functions - Reusable Blocks of Code
# This script introduces Python functions, which help organize code into reusable blocks.
# Functions make programs cleaner, easier to maintain, and reduce repetition.

# def greet(name):
#     return f"Hello, {name}"

# print(greet("Ashiqur"))


#calculator app:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b   

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator(num1, num2, op):
    op = op.strip()
    match op:
        case "+":
            return add(num1, num2)
        case "-":
            return subtract(num1, num2)
        case "*":
            return multiply(num1, num2)
        case "/":
            return divide(num1, num2)
        case _:
            return "Error: Invalid operator. Please use +, -, *, or /."



def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lower() == 'q':
            return None
        try:
            return float(value)
        except ValueError:
            print("Enter a number or 'q' to quit.")



while True:
    first_number = get_number("Enter first operand: ")
    if first_number is None:
        print("Goodbye!")
        break

    operator = input("Enter operator (+, -, *, /) or q to quit: ")

    if(operator.lower() == 'q'):
        print("Exiting calculator. Goodbye!")
        break

    second_number = get_number("Enter second operand: ")

    if second_number is None:
        print("Goodbye!")
        break

    result = calculator(first_number, second_number, operator)
    print(result)

