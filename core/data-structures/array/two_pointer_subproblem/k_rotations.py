class Solution:
    """
    Given an array arr and a non-negative number k, write a function to rotate the array by k steps to the RIGHT.
    Your function must do it by modifying the input array in-place i.e. you must do it in O(1) space complexity.
    Example 1

        Input: arr = [1, 2, 3, 4, 5], k = 3
        Output: [3, 4, 5, 1, 2]
        Explanation: Below are the rotations:
        Rotate 1 step to the right -> [5, 1, 2, 3, 4]
        Rotate 2 steps to the right -> [4, 5, 1, 2, 3]
        Rotate 3 steps to the right -> [3, 4, 5, 1, 2]
    """

    def reverse(self, arr: list[int], start: int, end: int) -> list[int]:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        return arr

    def k_rotations(self, arr: list[int], k: int) -> None:
        n = len(arr)
        k %= n

        self.reverse(arr, 0, n - 1)
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)


arr = [1, 2, 3, 4, 5]
print(arr)

solution = Solution()
solution.k_rotations(arr, 3)
print(arr)
