class Node:
    def __init__(self, data): self.data, self.next = data, None
top = None

def push(x):
    global top
    n = Node(x); n.next = top; top = n

def pop():
    global top
    if not top: print("Underflow")
    else: print("Popped:", top.data); top = top.next

def peek(): print(top.data if top else "Empty")

def display():
    p = top
    while p: print(p.data, end=" "); p = p.next
    print()

push(10); push(20); display(); peek(); pop(); display()

