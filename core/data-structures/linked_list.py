# Big O
# Append: O(1)
# Pop: O(n)
#   have to set pointer to new last node
# Prepend: O(1)
# Pop first: O(1)
# Insert: O(n)
# Remove: O(n)
# Lookup by index: O(n)
#   Must iterate through indexes
# Lookup by value: O(n)

# Lists better for pop and lookup by index
# LL better for prepend and pop first


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    # remove last node and return it
    # tail to new last node
    # edge empty
    # edge one
    def pop(self):
        if self.head is None:
            raise IndexError("Invalid index. Length of list is 0.")
        elif self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


ll = LinkedList(4)
ll.append(6)
ll.append(8)
ll.append(2)
ll.print_list()
print("--")
ll.prepend(5)

ll.print_list()
