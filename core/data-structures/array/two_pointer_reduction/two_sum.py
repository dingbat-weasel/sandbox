def two_sum(arr: list[int], target: int) -> list[int]:
    """
    Given an integer array arr and an integer target, write a function to check if two numbers exist in the array that sum up to the target. If such a pair exists, return them in an array, if not return an empty array. You can return the answer in any order.

    It is guaranteed that not more than one answer exists.

    Input: arr = [2, 8, 3, 6, 4], target = 7
    Output: [3, 4]
    Explanation: The numbers 3 and 4 sum up to make the target 7.
    """
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return [arr[left], arr[right]]

        elif arr[left] + arr[right] < target:
            left += 1

        else:
            right -= 1

    return []


print(two_sum([2, 8, 3, 6, 4], 7))
