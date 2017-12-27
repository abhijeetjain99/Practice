# Ttile: Basic Reverse Polish Notation Calculator
# Author: Pradeep Yadav
# Date: 27/12/2017

import math                            # imported to get factorial functionality

def evaluatePostfixExp(expression):
    # Function to evaluate postfix expressions with operation 
    # [+,-,*,/,power(^), Factorial(!), Percent(%)] and capable of hadling int
    # and float operands
    # Input: Postfix expression as String(Space separated)
    # Output: Result of expression
    
    expression = expression.split(' ')    # Separating tokens
    stack = []                            # Stack data structure to store operands
    for token in expression:
        if token == '+':                  # Checking for the operation to be performed
            oper1, oper2 = (stack.pop(), stack.pop())  # Getting operands
            result = oper2 + oper1
            stack.append(result)
        elif token == '*':
            oper1, oper2 = (stack.pop(), stack.pop())
            result = oper2 * oper1
            stack.append(result)
        elif token == '-':
            oper1, oper2 = (stack.pop(), stack.pop())
            result = oper2 - oper1
            stack.append(result)
        elif token == '/':
            oper1, oper2 = (stack.pop(), stack.pop())
            result = oper2 / oper1
            stack.append(result)
        elif token == '^':
            oper1, oper2 = (stack.pop(), stack.pop())
            result = oper2 ** oper1
            stack.append(result)
        elif token == '!':
            oper1 = stack.pop()
            result = math.factorial(int(oper1))
            stack.append(result)
        elif token == '%':
            oper1 = stack.pop()
            result = oper1/100
            stack.append(result)
        elif token.find('.') == -1:
            stack.append(int(token))
        else:
            stack.append(float(token))
    return(stack.pop())                         # Returning result                


def main():
    expression = input()
    print(evaluatePostfixExp(expression))
    

if __name__ == "__main__":
    main()
