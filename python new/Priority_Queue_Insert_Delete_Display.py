pq = []
def insert(item, priority):
    pq.append((priority, item))
    pq.sort(reverse=True)
def delete():
    print(pq.pop(0) if pq else "Empty")
def display(): print(pq)

insert("A", 2); insert("B", 5); insert("C", 1)
display(); delete(); display()

