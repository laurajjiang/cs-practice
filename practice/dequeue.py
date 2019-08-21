class Dequeue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addBack(self, item):
        self.items.insert(item)

    def removeFront(self, item):
        return self.items.pop()

    def removeBack(self, item):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
