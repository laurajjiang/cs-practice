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

    def search_node(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_node() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("data does not exist")
        return current

    def delete_node(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("data does not exist")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next_node(current.get_next())

