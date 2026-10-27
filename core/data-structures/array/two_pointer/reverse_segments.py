# Given a string s and an integer k, write a function
# that processes the string in groups of 2k characters,
# reversing the first k characters in each group, and returns the updated string.

# If fewer than k characters remain, reverse all remaining characters.
# If at least k but fewer than 2k characters remain,
# reverse only the first k characters and leave the rest unchanged.


class Solution:
    def reverse_segment(self, arr: list[str], left: int, right: int) -> None:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

    def reverse_segments(self, s: str, k: int) -> str:
        arr = list(s)
        start = 0
        n = len(arr)

        for start in range(0, n, 2 * k):
            left = start
            right = min(start + k - 1, n - 1)

            self.reverse_segment(arr, left, right)

        return "".join(arr)
