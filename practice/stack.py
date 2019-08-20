class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self, data):
        self.items.pop(data)

    def size(self):
        return len(self.items)
