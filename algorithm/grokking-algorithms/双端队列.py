class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.isEmpty())

d.addFront("ae")
d.addFront(1)
d.addRear([1])

print(d.size())
print(d.isEmpty())

d.addRear({1: "2"})

print(d.removeFront())
print(d.removeRear())

print(d.items)


