class Solution:
    def skip_duplicates_left(self, arr: list[int], left: int, right: int) -> int:
        while left < right and arr[left] == arr[left + 1]:
            left += 1

        return left + 1

    def skip_duplicates_right(self, arr: list[int], left: int, right: int) -> int:
        while left < right and arr[right] == arr[right - 1]:
            right -= 1

        return right - 1

    def duplicate_aware_two_sum(
        self, arr: list[int], left: int, target: int
    ) -> list[list[int]]:
        right = len(arr) - 1
        result = []

        while left < right:
            total = arr[left] + arr[right]

            if total == target:
                result.append([arr[left], arr[right]])

                left = self.skip_duplicates_left(arr, left, right)
                right = self.skip_duplicates_right(arr, left, right)

            elif total < target:
                left += 1

            else:
                right -= 1

        return result

    def four_sum(self, arr: list[int], target: int) -> list[list[int]]:
        result = []

        arr.sort()

        for i in range(len(arr)):
            # skip duplicates for the first el
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, len(arr)):
                # skip duplicates for second el
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                # define remaining target for tp technique
                remaining_target = target - arr[i] - arr[j]

                # find pairs with sum equal to remaining target
                two_sum_results = self.duplicate_aware_two_sum(
                    arr, j + 1, remaining_target
                )

                # add the quadruplets to the result
                for two_sum in two_sum_results:
                    result.append([arr[i], arr[j], two_sum[0], two_sum[1]])

        return result
