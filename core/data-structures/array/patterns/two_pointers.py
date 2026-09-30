"""
allows solving in linear time with single pass; traversing both directions simultaneously

1: initialize two var left and right such that left < right
2: loop while left < right
2.1: do some operations using arr[left] and arr[right] as needed
2.2: incr left by some steps if it should be increased
2.3: decr right by some steps if it should be decreased


The generic implementation uses helper functions incrementLeft and decrementRight (which decide, based on arr[left] and arr[right], whether each pointer should move in this iteration) and leftStep and rightStep (which decide by how many positions each pointer should move).

In most cases, these have a very simple implementation (for example, always return true and always return 1) and can be implemented inline where they are used.

The example bodies below use a placeholder condition based on the sum arr[left] + arr[right] only to show the shape; concrete problems will replace these conditions with their own.

Complexity:
    The two pointers move simultaneously from both ends and meet in the middle, performing a full arr traversal. So, time is of linear complexity where n is the size of the array.

    No new data structure so space is constant.

    Best Case:
        Space: O(1)
        Time: O(n)
    Worst Case:
        Space: O(1)
        Time: O(n)
"""


class Solution:
    # generic
    def two_pointer(self, arr: list[int]) -> None:

        # initialize left and right to the ends of the arr
        left = 0
        right = len(arr) - 1

        while left < right:
            left_val = arr[left]
            right_val = arr[right]

            # check if the left pointer should be incremented
            if self.increment_left(left_val, right_val):
                # incr the left pointer by some steps
                left += self.left_step(left_val, right_val)

            # check if the right pointer should be incremented
            if self.decrement_right(left_val, right_val):
                # decr the right pointer by some steps
                right -= self.right_step(left_val, right_val)

    # decide whether to move the left pointer
    def increment_left(self, left_val: int, right_val: int) -> bool:
        # example condition: move left if sum < 10
        return left_val + right_val < 10

    # decide whether to move the right pointer
    def decrement_right(self, left_val: int, right_val: int) -> bool:
        # example condition: move right if sum > 10
        return left_val + right_val > 10

    # steps to move the left pointer
    def left_step(self, left_val: int, right_val: int) -> int:
        return 1  # example: move 1 step

    # steps to move the right pointer
    def right_step(self, left_val: int, right_val: int) -> int:
        return 1  # example: move 1 step
