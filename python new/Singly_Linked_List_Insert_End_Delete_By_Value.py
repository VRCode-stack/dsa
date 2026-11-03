class Node:
    def __init__(self, data): self.data, self.next = data, None
head = None

def insert_end(x):
    global head
    n = Node(x)
    if not head: head = n; return
    p = head
    while p.next: p = p.next
    p.next = n

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

insert_end(10); insert_end(20); insert_end(30)
delete_value(20); display()


