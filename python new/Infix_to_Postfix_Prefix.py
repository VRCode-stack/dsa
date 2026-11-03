def precedence(op): return {'+':1, '-':1, '*':2, '/':2, '^':3}.get(op, 0)

def to_postfix(s):
    out, st = "", []
    for ch in s.replace(" ", ""):
        if ch.isalnum(): out += ch
        elif ch == '(': st.append(ch)
        elif ch == ')':
            while st and st[-1] != '(': out += st.pop()
            st.pop()
        else:
            while st and st[-1] != '(' and precedence(st[-1]) >= precedence(ch):
                out += st.pop()
            st.append(ch)
    while st: out += st.pop()
    return out

def to_prefix(s):
    rev = s[::-1].replace('(', '#').replace(')', '(').replace('#', ')')
    p = to_postfix(rev)
    return p[::-1]

exp = input("Infix (example A+B*C): ")
print("Postfix:", to_postfix(exp))
print("Prefix:", to_prefix(exp))
# Note: use single-character operands for this short practical version.
