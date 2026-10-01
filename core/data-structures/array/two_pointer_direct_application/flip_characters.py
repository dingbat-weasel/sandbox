# given an array of characters arr, write a function
# that reverses the given array by swapping
# equidistant elements from the start and the end
# must modify the input arr in-place; O(1) space complexity


class Solution:
    def flip_characters(self, arr: list[str]) -> None:
        left: int = 0
        right: int = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1
