# given an array of characters arr, write a function
# that reverses the given array by swapping
# equidistant elements from the start and the end
# must modify the input arr in-place; O(1) space complexity


def flip_characters(arr: list[str]) -> None:
    left: int = 0
    right: int = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


class Solution:
    def flip_characters(self, arr: list[str]) -> None:

        # Initialize two pointers, one pointing to the beginning of the
        # string and the other pointing to the end of the string
        left: int = 0
        right = len(arr) - 1

        # Use a while loop to traverse the string using the two pointers
        while left < right:
            # Swap the characters pointed by the left and right pointers
            arr[left], arr[right] = arr[right], arr[left]

            # Move the pointers towards the center of the string
            left += 1
            right -= 1
