#!/usr/bin/env python3

import operator
from colorama import init, Fore

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def coloredprint(x):
    if (x < 0):
        print(Fore.RED + str(x) + Fore.WHITE)
    elif (x == 0):
        print(Fore.BLUE + str(x) + Fore.WHITE)
    else:
        print(Fore.GREEN + str(x) + Fore.WHITE)

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
            print(Fore.CYAN + str(token), end=" ")
        except ValueError:
            function = operators[token]
            print(Fore.MAGENTA + token + Fore.WHITE, end=" ")
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    print()
    return stack.pop()

def dumbfunc():
    print("wow this function does nothing")
    
def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", end=" ")
        coloredprint(result)

if __name__ == '__main__':
    main()
