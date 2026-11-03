def precedence(op):
    if op == '^':
        return 3
    if op in '*/':
        return 2
    if op in '+-':
        return 1
    return 0


def should_pop(top, cur, prefix_mode):
    if precedence(top) > precedence(cur):
        return True
    if precedence(top) == precedence(cur):
        if prefix_mode:
            return cur == '^'
        return cur != '^'
    return False


def to_postfix(expr, prefix_mode=False):
    stack = []
    result = ""
    for ch in expr:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and should_pop(stack[-1], ch, prefix_mode):
                result += stack.pop()
            stack.append(ch)
    while stack:
        result += stack.pop()
    return result


def to_prefix(expr):
    reversed_expr = ""
    for ch in expr[::-1]:
        if ch == '(':
            reversed_expr += ')'
        elif ch == ')':
            reversed_expr += '('
        else:
            reversed_expr += ch
    return to_postfix(reversed_expr, True)[::-1]


expressions = ["A+B*C", "(A+B)*C", "A+B*C-D/E", "(A+B)*(C-D)", "A^B^C"]
for e in expressions:
    print("Infix   :", e)
    print("Postfix :", to_postfix(e))
    print("Prefix  :", to_prefix(e))
    print()
