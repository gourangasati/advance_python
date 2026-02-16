#infix - left root right
#postfix- left right root
#prefix - root left right 

def is_operator(c):
    return c in "+-*/^"

def precedence(op):
    if op == '^':
        return 3
    if op in "*/":
        return 2
    if op in "+-":
        return 1
    return 0

def infix_to_postfix(expr):
    stack = []
    output = []
    for ch in expr:
        if ch.isalnum():   
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while stack and precedence(stack[-1]) >= precedence(ch):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())

    return "".join(output)

def infix_to_prefix(expr):
    expr = expr[::-1]
    expr = expr.replace('(', '#').replace(')', '(').replace('#', ')')
    postfix = infix_to_postfix(expr)
    return postfix[::-1]

def postfix_to_infix(expr):
    stack = []
    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a}{ch}{b})")
    return stack[-1]

def prefix_to_infix(expr):
    stack = []

    for ch in reversed(expr):
        if ch.isalnum():
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{ch}{b})")

    return stack[-1]

def postfix_to_prefix(expr):
    stack = []

    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(ch + a + b)

    return stack[-1]

def prefix_to_postfix(expr):
    stack = []

    for ch in reversed(expr):
        if ch.isalnum():
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + ch)

    return stack[-1]

expr = "(A+B)*C"

print("Infix:", expr)
print("Postfix:", infix_to_postfix(expr))
print("Prefix:", infix_to_prefix(expr))

pf = "AB+C*"
print("\nPostfix:", pf)
print("Infix:", postfix_to_infix(pf))
print("Prefix:", postfix_to_prefix(pf))

pre = "*+ABC"
print("\nPrefix:", pre)
print("Infix:", prefix_to_infix(pre))
print("Postfix:", prefix_to_postfix(pre))
