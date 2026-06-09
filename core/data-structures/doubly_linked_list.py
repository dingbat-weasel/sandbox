from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    # better practice to use sentinel head and tail nodes, see proper class below
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
        if self.tail is None:
            return None
        temp = self.tail
        self.length -= 1

        if self.tail.prev is None:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None

        temp = self.head
        self.length -= 1

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()
print("--")
dll.pop_first()
dll.print_list()


class DLL_BetterDesign:
    def __init__(self):
        # Sentinel Design: Head and Tail always exist, eliminating Null checks
        self._sentinel_head = Node(None)
        self._sentinel_tail = Node(None)
        self._sentinel_head.next = self._sentinel_tail
        self._sentinel_tail.prev = self._sentinel_head
        self._length = 0

    def _get_node_at(self, index: int) -> Node:
        """Internal helper: Always returns a Node or raises an Exception."""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range.")

        # Optimization: Start from head or tail depending on which is closer
        if index < self._length // 2:
            curr = self._sentinel_head.next

            for _ in range(index):
                # the two options for handling curr.next or prev type errors
                assert curr is not None  # asserts at runtime
                curr = curr.next
        else:
            curr = self._sentinel_tail.prev
            for _ in range(self._length - 1 - index):
                curr = curr.prev  # type: ignore

        assert curr is not None
        return curr

    def get(self, index: int) -> Any:
        """Public API: Only exposes values, completely hiding Node tracking."""
        return self._get_node_at(index).value

    def append(self, value: Any) -> None:
        """Public API: Clean, structural updates without edge cases."""
        new_node = Node(value)
        old_last = self._sentinel_tail.prev

        assert old_last is not None

        # Stitching connections
        new_node.next = self._sentinel_tail
        new_node.prev = old_last

        old_last.next = new_node
        self._sentinel_tail.prev = new_node

        self._length += 1
