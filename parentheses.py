# parentheses.py will output the string yes if the input is a string with balanced parentheses and no if it is not.
# input will look like: python3 parentheses.py "(()()(()))"

import sys

def isBalanced(inputS):
    numOpenParen = inputS.count('(') # Count the number of times each appear in the string inputS
    numCloseParen = inputS.count(')')
    
    return (numOpenParen == numCloseParen) # return true or false

# Check for invalid num of args
if len(sys.argv) != 2:
    raise Exception("Invalid number of arguments.")
# If valid,
else:
    input = sys.argv[1] # Get the string to test
    # Check if the parentheses are balanced
    if isBalanced(input):
        print("yes")
    else:
        print("no")
