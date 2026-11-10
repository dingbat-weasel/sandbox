def target_limited_two_sum(arr: list[int], target: int) -> int:
    """
    Given an array arr consisting of non-negative integers and an integer target, write a function to find the largest possible sum of two elements at different indices in the array that is strictly less than the target. If no such pair exists, return -1 instead.

    Input: arr = [34, 23, 1, 24, 75, 33, 54, 8], target = 60
    Output: 58
    Explanation: We can use 34 and 24 to sum 58, which is less than 60.
    """
    out = -1
    if len(arr) == 0:
        return out

    arr.sort()

    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]

        if sum < target:
            out = max(out, sum)
            left += 1

        else:
            right -= 1

    return out


print(target_limited_two_sum([5, 5, 5], 11))
