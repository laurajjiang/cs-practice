class Node(object):
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next = next_node
        self.previous = previous_node

    def get_node(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_next_node(self, new_node):
        self.next_node = new_node


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def get_size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        return size

    def insert_front(self, data):
        if self.head == None:
            new_node = data
            self.head = new_node
        else:
            new_node = data
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp

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
        temp = self.head
        if temp.next != None:
            if temp.data == data:
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
            else:
                while temp.next != None:
                    if temp.data == data:
                        break
                    temp = temp.next
                if temp.next != None:
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    temp.previous.next = None
                    temp.previous = None
