class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        print("Inserted", item, "with priority", priority)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty!")
            return
        highest = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[highest][1]:
                highest = i
        item, priority = self.queue.pop(highest)
        print("Removed", item, "with priority", priority)

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        print("Queue (item, priority):", self.queue)


pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 4)
pq.enqueue("Task D", 2)
pq.display()
pq.dequeue()
pq.dequeue()
pq.display()
pq.dequeue()
pq.dequeue()
pq.dequeue()
