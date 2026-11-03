stack = []
def push(x): stack.append(x)
def pop():
    print(stack.pop() if stack else "Stack Underflow")
def peek():
    print(stack[-1] if stack else "Stack Empty")
def display(): print(stack)

push(10); push(20); display(); peek(); pop(); display()


