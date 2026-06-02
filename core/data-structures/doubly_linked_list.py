class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    head: Node | None
    tail: Node | None

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        elif temp and temp.prev:
            new_tail = temp.prev
            self.tail = new_tail
            new_tail.next = None
            temp.prev = None

        self.length -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()
print("--")
dll.pop()
dll.print_list()
