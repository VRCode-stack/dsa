class Node:
    def __init__(self, data):
        self.data, self.prev, self.next = data, None, None
head = None

def insert_pos(x, pos):
    global head
    n = Node(x)
    if pos == 0:
        n.next = head
        if head: head.prev = n
        head = n; return
    p = head
    for _ in range(pos - 1):
        if not p: print("Invalid position"); return
        p = p.next
    if not p: print("Invalid position"); return
    n.next = p.next; n.prev = p
    if p.next: p.next.prev = n
    p.next = n

def delete_end():
    global head
    if not head: return
    p = head
    while p.next: p = p.next
    if p.prev: p.prev.next = None
    else: head = None

def display():
    p = head
    while p: print(p.data, end=" <-> "); p = p.next
    print("None")

insert_pos(10, 0); insert_pos(20, 1); insert_pos(15, 1)
delete_end(); display()

