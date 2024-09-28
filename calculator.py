# calculator.py will take an arithmetic expression built from numbers, parentheses and operations +, *, ^.
# input will look like: 
# python3 calculator.py "1+2+3+4" --> 10
# python3 calculator.py "1+2*3" --> 7
# python3 calculator.py "1+2*3+4*5*6" --> 127
# python3 calculator.py "(1+2)*3" --> 9
# python3 calculator.py "(1+2*(3+4*(5+6)))*2" --> 190
# python3 calculator.py "2^3" --> 8

import sys

# Functions that perform the math
def add(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def exp(num1, num2):
    return num1 ** num2

# Does the calculator
# This method is crucial as it performs recursion if it finds an expression within the parenthesis
def calculate(exp):
    # This method goes down the precedence in order

    # Find innermost parenthesis first
    while '(' in exp:
        start = exp.rfind('(')
        end = exp.find(')', start)
        innerResult = calculate(exp[start + 1:end])
        exp = exp[:start] + str(innerResult) + exp[end + 1:]

    # Then check for exponents
    chars = exp.split()
    i = 0
    while i < len(chars):
        if chars[i] == '^':
            result = exp(int(chars[i - 1]), int(chars[i + 1]))
            # Replace expression w result
            chars[i - 1:i + 2] = [str(result)] 
        else:
            i += 1

    # Then check for multiplication the exact same way
    # reset the index
    i = 0
    while i < len(chars):
        if chars[i] == '*':
            result = mult(int(chars[i - 1]), int(chars[i + 1]))
            # Replace expression w result
            chars[i - 1:i + 2] = [str(result)]
        else:
            i += 1

    # Finally, check for addition

    i = 0
    result = int(chars[i])
    i += 1
    while i < len(chars):
        if chars[i] == '+':
            result = add(result, int(chars[i + 1]))
        i += 2

    return result

# Check for invalid num of args
if len(sys.argv) != 2:
    raise Exception("Invalid number of arguments.")
# If valid,
else:
    inputExp = sys.argv[1] # Get the string to test

    # Add whitespace to perform operations
    # Rename expression as its now the expression from input
    inputExp = input.replace('+', ' + ').replace('*', ' * ').replace('^', ' ^ ')
    print(calculate(inputExp)) # Print result
    