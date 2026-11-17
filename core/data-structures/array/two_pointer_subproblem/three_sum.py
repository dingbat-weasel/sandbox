class Solution:
    """
    Given an integer array arr, write a function that returns all the triplets [arr[i], arr[j], arr[k]] such that i != j, i != k, and j != k, and arr[i] + arr[j] + arr[k] == 0. You can return the answer in any order.
    Notice that the solution set must not contain duplicate triplets.
    Example 1

        Input: arr = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]
        Explanation: [-1, -1, 2] and [-1, 0, 1] are the two eligible triplets that sum to 0.
    """

    def two_sum(self, arr: list[int], i: int, target) -> list[list[int]]:
        out = []
        left = 0
        right = len(arr) - 1

        while left < right:
            if left == i:
                left += 1

            elif right == i:
                right -= 1

            elif arr[left] + arr[right] == target:
                out.append([arr[left], arr[right]])

            elif arr[left] + arr[right] < target:
                left += 1

            else:
                right -= 1

        return out

    def three_sum(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        out = []

        for i in range(len(arr)):
            two_sum_target = 0 - arr[i]
            solutions = self.two_sum(arr, i, two_sum_target)

            out.extend(solutions)
            print(solutions, out)

        return out


solution = Solution()

print(solution.three_sum([-2, -1, 0, 1, 2, 3]))
