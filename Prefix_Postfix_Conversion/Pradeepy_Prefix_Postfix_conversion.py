# Title: Program to convert an infix expression to corresponding postfix 
# and prefix notation
# Author: Pradeep Yadav
# Date: 29/12/2017

def infixToPostfix(exp):
    # Function to convert infix expressions to postfix expressions
    # Input: exp :Infix expression as string
    # Return: Equivalent postfix expression 
    
    # stack to temporary store operators
    stack = []                            
    # Setting operator precedence
    prec = {"^":3, "*":2, "/":2, "%":2, "+":1, "-":1, "(":0 }
    result = str()                                  # String to store result  
    
    for token in exp.split(" "):
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack != []:
                tok = stack.pop()                   # poping stack untill 
                if tok == '(':                      # matching ( is found
                    break
                result += ' ' + tok
        elif token in prec.keys():
            if stack == []:                         # Push to stack if it is 
                stack.append(token)                 # empty
            else:
                stackTop = stack.pop()
                if prec[token] > prec[stackTop]:
                    stack.append(stackTop)          # push to stack if precedence 
                    stack.append(token)             # higher than top of stack
                else:
                    while prec[token] <= prec[stackTop] and stackTop != '(' and stack != []:
                        result += ' ' + stackTop    # Popping stack until a operator with
                        stackTop = stack.pop()      # lower precedence is found
                    stack.append(stackTop)          
                    stack.append(token)             # Pushing the token
        else:
            result += ' ' + token                   # Push operands to result
                
    while stack != []:                              # pop all the leftover 
        result += " " + stack.pop()                 # elements
        
    return result

def infixToPrefix(exp):
    # Function to convert an infix expression to prefix expression
    # Input: Expression in infix notation
    # Return: Equivalent expression in prefix notation
    
    exp = exp[::-1]                                 # Reverse the input string
    expList = list(exp)
    
    for index in range(len(expList)):
        if expList[index] == '(':                   # interschange the 
            expList[index] = ')'                    # parenthesis
        elif expList[index] == ')':
            expList[index] = '('
        else:
            pass
        
    exp = "".join(expList)
    return(infixToPostfix(exp)[::-1])              # convert to postfix and reverse
    

def main():
    expression = input("Enter expression(Space Separated):")
    
    expPostfix = infixToPostfix(expression)
    print("Postfix: " + expPostfix)
    
    expPrefix = infixToPrefix(expression)
    print("Preffix: " + expPrefix)

if __name__ == "__main__":
    main()
