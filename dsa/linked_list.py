class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_to_head(self, value):
        new_node = Node(value)
        new_node.next_element = self.head
        self.head = new_node.data
        return self.head

    def insert_to_tail(self, value):
        new_node = Node(value)
        temp = self.head.new_element

        while temp is not None:
            temp = temp.next_element
        temp.next_element = new_node
        return temp.next_element


linked_list = LinkedList()
linked_list.insert_to_head("Baby")
print(linked_list.get_head())
# linked_list.insert_to_tail("op")
# print(linked_list.get_head())
