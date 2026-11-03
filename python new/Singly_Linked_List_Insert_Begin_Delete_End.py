class Node:
    def __init__(self, data):
        self.data, self.next = data, None

head = None
def insert_begin(x):
    global head
    n = Node(x); n.next = head; head = n

def delete_end():
    global head
    if not head: print("Empty"); return
    if not head.next: head = None; return
    p = head
    while p.next.next: p = p.next
    p.next = None

def display():
    p = head
    while p: print(p.data, end=" -> "); p = p.next
    print("None")

insert_begin(10); insert_begin(20); display()
delete_end(); display()


