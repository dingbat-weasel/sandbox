class Solution:
    """
    Given an integer array arr and an integer target, write a function to find three integers in arr such that the sum is closest to the target. You must return the sum of the three integers.
    If there are more than one answers possible, pick the smaller one.
    Example 1

        Input: arr = [2, 7, 11, 15], target = 3
        Output: 20
        Explanation: 2 + 7 + 11 = 20 is the sum of three numbers that are closest to the target.
    """

    def closest_two_sum(self, arr: list[int], index: int, target: int) -> int:
        left = index + 1
        right = len(arr) - 1
        closest_total = float("inf")

        while left < right:
            total = arr[index] + arr[left] + arr[right]
            difference = abs(total - target)
            closest_difference = abs(closest_total - target)

            # update closest_total if the sum is strictly closer,
            # or equally close and smaller
            if difference < closest_difference or (
                difference == closest_difference and total < closest_total
            ):
                closest_total = total

            if total == target:
                return total

            elif total < target:
                left += 1

            else:
                right -= 1

        assert isinstance(closest_total, int)
        return closest_total

    def approximate_three_sum(self, arr: list[int], target: int) -> int:
        arr.sort()

        closest_total = float("inf")
        for i in range(len(arr)):
            current_total = self.closest_two_sum(arr, i, target)

            difference = abs(current_total - target)
            closest_difference = abs(closest_total - target)

            if difference < closest_difference or (
                difference == closest_difference and current_total < closest_total
            ):
                closest_total = current_total

        assert isinstance(closest_total, int)
        return closest_total


solution = Solution()
