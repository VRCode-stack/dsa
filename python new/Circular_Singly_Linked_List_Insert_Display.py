class Node:
    def __init__(self, data): self.data, self.next = data, None
last = None

def insert(x):
    global last
    n = Node(x)
    if not last: n.next = n; last = n
    else: n.next = last.next; last.next = n; last = n

def display():
    if not last: print("Empty"); return
    p = last.next
    while True:
        print(p.data, end=" -> ")
        p = p.next
        if p == last.next: break
    print("(back to start)")

insert(10); insert(20); insert(30); display()
