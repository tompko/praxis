import operator

operators = {"+": operator.add,
             "-": operator.sub,
             "/": operator.div,
             "*": operator.mul}

def calc_rpn(rpn):
    rpn = rpn.split(" ")

    stack = []

    for term in rpn:
        if term in operators:
            func = operators[term]
            b, a = stack.pop(), stack.pop()
            res = func(a, b)
            stack.append(res)
        else:
            stack.append(float(term))

    return stack[-1]
