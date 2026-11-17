class Solution:
    """
    Given an integer array arr, write a function that returns all the triplets [arr[i], arr[j], arr[k]] such that i != j, i != k, and j != k, and arr[i] + arr[j] + arr[k] == 0. You can return the answer in any order.
    Notice that the solution set must not contain duplicate triplets.
    Example 1

        Input: arr = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]
        Explanation: [-1, -1, 2] and [-1, 0, 1] are the two eligible triplets that sum to 0.
    """

    def skip_duplicates_left(self, arr: list[int], left: int, right: int) -> int:

        # skip duplicates from the left pointer
        while left < right and arr[left] == arr[left + 1]:
            left += 1

        return left + 1

    def skip_duplicates_right(self, arr: list[int], left: int, right: int) -> int:

        # skip duplicates from the right pointer
        while left < right and arr[right] == arr[right] - 1:
            right -= 1

        return right - 1

    def duplicate_aware_two_sum(
        self, arr: list[int], index: int, result: list[list[int]]
    ) -> None:
        left = index + 1
        right = len(arr) - 1

        while left < right:
            total = arr[index] + arr[left] + arr[right]

            # if sum is 0, add the triplet to result
            if total == 0:
                result.append([arr[index], arr[left], arr[right]])

                # move left to next unique element
                left = self.skip_duplicates_left(arr, left, right)

                # move right to next unique element
                right = self.skip_duplicates_right(arr, left, right)

            elif total < 0:
                left += 1

            else:
                right -= 1

    def three_sum(self, arr: list[int]) -> list[list[int]]:
        result = []

        # sort the arr in non-decreasing order
        arr.sort()

        # traverse the arr using 1 pointer
        for i in range(len(arr)):
            # skip duplicates for the first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # use the two-pointer technique to find pairs
            # with sum -arr[i]
            self.duplicate_aware_two_sum(arr, i, result)

        return result


solution = Solution()

print(solution.three_sum([-2, -1, 0, 1, 2, 3]))
