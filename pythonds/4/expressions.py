from ds_implementation import Stack

def infixToPostfix(expr: str) -> str: 
    operatorStack = Stack()
    precedence = {}
    precedenceOf["*"] = 3,  precedenceOf["/"] = 3
    precedenceOf["+"] = 2,  precedenceOf["-"] = 2
    precedenceOf["("] = 1

    postfix = []
    tokens = expr.split()

    for token in tokens: 
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix.push(token)
        elif token == '(':
            operatorStack.push(token)
        elif token == ')':
            op = operatorStack.pop()
            while op != '(':
                postfix.append(op)
                op = operatorStack.pop()
        else: 
            while (not operatorStack.isEmpty()) and (precendeceOf[operatorStack.peek()] >= precedenceOf[token]):
                postfix.append(operatorStack.pop())
            operatorStack.push(token)
   
def postfixToInfix(expr: str) -> str:
    

def evalExpression(): pass