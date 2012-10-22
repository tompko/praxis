"""RPN Calculator: Evaluate numeric expressions at the command line"""

import sys
import operator

OPERATORS = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.div}

def rpn(expr, stack=None):
    """Evaluate an expression in reverse polish notation"""
    if stack == None:
        stack = []

    expr = expr.split()

    for e in expr:
        if e in OPERATORS:
            b, a = stack.pop(), stack.pop()
            stack.append(OPERATORS[e](a, b))
        else:
            stack.append(float(e))

    return stack

if __name__ == "__main__":
    #Read expressions from standard input and print the top of the stack
    #to standard output when a newline is encountered
    STACK = []
    LINE = sys.stdin.readline()
    while LINE.strip():
        STACK = rpn(LINE.strip(), STACK)
        print STACK[-1]
        LINE = sys.stdin.readline()
