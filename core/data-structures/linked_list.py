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
# self better for prepend and pop first


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

    def pop_first(self):
        if self.head is None:
            raise IndexError("Invalid index. Length of list is 0.")

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # len 1 -> 0
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(f"Invalid index. Length of list is {self.length}.")

        temp = self.head
        for _ in range(index):
            if temp is None:
                raise IndexError(f"Invalid index. Length of list is {self.length}.")
            temp = temp.next

        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(f"Invalid index. Length of list is {self.length}.")

        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError(f"Invalid index. Length of list is {self.length}.")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        if temp is not None:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        if prev is None:
            return False

        temp = prev.next
        if temp is None:
            return False

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            if temp and temp.next:
                after = temp.next
                temp.next = before
            before = temp
            temp = after

    # from here are some leetcode-esque methods as practice
    def find_middle_node(self):
        if self.head == None:
            return None

        slow = self.head
        fast = self.head

        # AND uses short circuiting to eval
        # fast.next not None AND fast not None produces error, no prop .next on Nonetype
        # eval fast first, determines it None and doesn't check second condition, prevents error
        while fast is not None and fast.next is not None:
            if slow:
                slow = slow.next
            fast = fast.next.next

        if slow == None:
            return None
        return slow.value

    def has_loop(self):
        if self.head == None:
            return None

        slow = self.head
        fast = self.head
        while fast and fast.next:
            if slow:
                slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def remove_duplicates(self):
        if self.head == None:
            return None
        seen = set()

        previous = self.head
        current = previous.next
        seen.add(previous.value)
        while current:
            if current.value in seen:
                previous.next = current.next
                self.length -= 1
            else:
                seen.add(current.value)
                previous = current
            current = current.next


def kth_from_end(ll, k):
    if ll.head == None:
        return None

    slow = ll.head
    fast = ll.head
    for _ in range(k - 1):
        if fast == None:
            return None
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    return slow


LL = LinkedList(4)
LL.append(6)
LL.append(8)
LL.append(6)
LL.append(6)
LL.append(3)
LL.append(8)

LL.print_list()
print("--")
seen = LL.remove_duplicates()
LL.print_list()
print("--")
