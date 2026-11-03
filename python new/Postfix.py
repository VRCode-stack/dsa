def evaluate(exp):
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                r = a + b
            elif ch == '-':
                r = a - b
            elif ch == '*':
                r = a * b
            elif ch == '/':
                r = a // b
            elif ch == '^':
                r = a ** b
            stack.append(r)
            print(a, ch, b, "=", r)
    return stack.pop()


for exp in ["23*54*+", "231*+9-"]:
    print("Postfix Expression:", exp)
    print("Result:", evaluate(exp))
    print()
