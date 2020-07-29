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
   
def postfixEval(expr: str) -> str:
    operandStack = Stack()
    tokens = expr.split()

    for token in tokens: 
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            res = calculate(token, op1, op2)
            operandStack.push(res)
    return operandStack.pop()

def calculate(op: chr, op1: int, op2: int) -> int:
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2