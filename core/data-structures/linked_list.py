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
        self.next = None


class LinkedList:
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


ll1 = LinkedList(4)
ll1.print_list()
