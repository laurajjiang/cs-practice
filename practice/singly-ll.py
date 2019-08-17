class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_node(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def get_size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        return size

