class Node:
    def __init__(self, data):
        self.data, self.prev, self.next = data, None, None
head = None

def insert_begin(x):
    global head
    n = Node(x); n.next = head
    if head: head.prev = n
    head = n

def delete_value(x):
    global head
    p = head
    while p and p.data != x: p = p.next
    if not p: return
    if p.prev: p.prev.next = p.next
    else: head = p.next
    if p.next: p.next.prev = p.prev

def display():
    p = head
    while p: print(p.data, end=" <-> "); p = p.next
    print("None")

insert_begin(10); insert_begin(20); delete_value(10); display()


