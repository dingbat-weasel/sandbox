"""
Problem: find middle node

Description:
Identify middle node of LL
- No length counter available
- Cannot count list
- Can only loop once

Approach:
two pointers, slow and fast
as we loop through the LL:
- slow moves one node
- fast moves two
odd length: fast on last node, next is none, slow = middle
even length: fast on last + 1 node, last is none, slow = first node in right side of ll
"""


class Node:
    def __init__(self, value):
        self.value: int = value
        self.next: None | Node = None


class LL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


test_ll1 = LL(1)
test_ll1.append(2)
test_ll1.append(3)
test_ll1.append(4)
test_ll1.append(5)

test_ll2 = LL(1)
test_ll2.append(2)
test_ll2.append(3)
test_ll2.append(4)


def find_middle_node(LL):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if LL.head == None:
        return None

    slow = LL.head
    fast = LL.head

    # AND uses short circuiting to eval
    # fast.next not None AND fast not None produces error, no prop .next on Nonetype
    # eval fast first, determines it None and doesn't check second condition, prevents error
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.value


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        # (input, expected_output),
        (test_ll1, 3),
        (test_ll2, 3),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = find_middle_node(input_data)
        status = "✓" if result == expected else "✗"
        print(
            f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}"
        )
