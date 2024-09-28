specs.md contains detailed specifications of the implementation of the code. It contains the names of the methods used and their purpose, and in general outlines the internal logic of these methods as well as the general logic of the program flow.

parentheses.py:
- isBalanced(inputS) takes in a string and checks the amount of left and right parenthesis characters in the string. The function returns a boolean: true if the number is equal, and false if the number is unequal. 
- The program continues by checking that the correct number of command line arguments is passed in. If not, the program throws an error. 
- If the amount of arguments is valid, the else statement is entered, and the program gets the string from the command line, and runs it through the isBalanced() function. If it is balanced, the program returns yes. If not, it returns no.

calculator.py
- add(num1, num2) adds two numbers and returns the result. 
- mult(num1, num2) multiplies two numbers and returns the result.
- exp(num1, num2) raises num1 to the power of num2 and returns the result.
- calculate(exp) does a number of things in order of operator precedence. Calculate is used recursively to traverse the string and ensure the rules of precedence are followed. 
    - The first block of code enters a while loop. If there exists an opening parenthesis in exp (the expression passed into the function), start and end define where those parentheses are. The while loop recursively calls calculate, repeating this process again in the event that there are mutliple sets of parentheses. The final line of the while loop replaces the expression with the result. 
    - Next, the function begins to check for exponents. It first splits the expression into individual characters, or chars (the name of the variable). The function loops through every character in the expression, and if it reaches an exponent symbol, it will evaluate it and replace the expression with the result. If it never reaches an exponent symbol, it keeps looping. Once it makes it through the entire string after evaluating what was needed, it moves on to the next block of code. 
    - The next block of code will check for multiplication in the exact same way.
    - The same is for addition. The idea is that by setting it up in this order, it will follow the order of operations. When the paretheses block calls the calculate function recursively, it will follow this order too. 
- Now, to enter the "main method", the program checks that the correct number of command line arguments is passed in. If not, the program throws an error. 
- If the amount of arguments is valid, the else statement is entered, and the program gets the string from the command line, and replaces each operation with itself, just containing whitespace around it. The purpose of this is 
that while expressions are being replaced and calculated, indices are not mixed up or parsed incorrectly. 
- Finally, the calculate method is called on the input expression, inputExp, and the result is printed.