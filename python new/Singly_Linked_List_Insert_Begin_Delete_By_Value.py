class Node:
    def __init__(self, data): self.data, self.next = data, None
head = None

def insert_begin(x):
    global head
    n = Node(x); n.next = head; head = n

def delete_value(x):
    global head
    if not head: return
    if head.data == x: head = head.next; return
    p = head
    while p.next and p.next.data != x: p = p.next
    if p.next: p.next = p.next.next

def display():
    p = head
    while p: print(p.data, end=" -> "); p = p.next
    print("None")

insert_begin(10); insert_begin(20); delete_value(10); display()


