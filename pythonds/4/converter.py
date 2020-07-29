from ds_implementation import Stack

def divideBy2(number: int) -> str: 
    s = Stack()

    while number > 0:
        rem = number % 2
        s.push(rem)
        number //= 2
    
    binString = ""
    while not s.isEmpty():
        binString += s.pop()
    
    return binString

def baseConverter(number: int, base: int) -> str: 
    dig = "0123456789ABCDEF"
    s = Stack()

    while number > 0:
        rem = number % base
        s.push(rem)
        number //= base

    binString = ""
    while not s.isEmpty():
        binString += dig[s.pop()]
        
    return binString