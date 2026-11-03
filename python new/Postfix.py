exp = input("Postfix (example 23*54*+): ")
st = []
for ch in exp:
    if ch.isdigit(): st.append(int(ch))
    else:
        b, a = st.pop(), st.pop()
        if ch == '+': st.append(a + b)
        elif ch == '-': st.append(a - b)
        elif ch == '*': st.append(a * b)
        elif ch == '/': st.append(a / b)
print("Result:", st[-1])


