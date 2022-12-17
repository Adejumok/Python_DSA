class Node:
    data = None

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "Node(%s)" % self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        present = self.head
        linked_list = []

        while present:
            if present == self.head:
                linked_list.append("Head: (%s)" % present.data)
            elif present.next_node is None:
                linked_list.append("Tail: (%s)" % present.data)
            else:
                linked_list.append("(%s)" % present.data)

            present = present.next_node

        return ' => '.join(linked_list)

    def size(self):
        present = self.head
        count = 0

        while present:
            present = present.next_node
            count += 1
        return count

    def prepend(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, value):
        new = Node(value)
        present = self.head

        while present:
            if present.next_node is None:
                present.next_node = new
                new.next_node = None
            present = present.next_node

    def insert(self, value, index):
        if index == 1:
            self.prepend(value)

        present = self.head
        new_node = Node(value)
        count = 1
        while present:
            if count == index - 1:
                temp_node = present.next_node
                present.next_node = new_node
                new_node.next_node = temp_node
            present = present.next_node
            count += 1

    def remove(self, index):
        count = 1
        present = self.head
        previous = None
        while present:
            if count == index:
                previous.next_node = present.next_node

            previous = present
            present = present.next_node
            count += 1

    def pop(self):
        present = self.head
        previous = None
        while present:
            if present.next_node is None:
                previous.next_node = present.next_node

            previous = present
            present = present.next_node


l = LinkedList()
l.prepend("Gbera Dide!")
l.prepend("Jare")
l.prepend("Omo")
l.append("Odiks")
l.insert("Wana", 3)
print(l)
print(l.size())
l.pop()
print(l)
l.remove(2)
print(l)
