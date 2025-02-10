class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())
q.enqueue("1")
q.enqueue("a")
q.enqueue([2])
q.enqueue({1:"dog"})
print(q.isEmpty())
print(q.items)
print(q.size())
q.dequeue()
q.dequeue()
print(q.size())
print(q.items)