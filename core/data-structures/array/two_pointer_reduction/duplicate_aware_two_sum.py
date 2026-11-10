def duplicate_aware_two_sum(arr: list[int], target: int) -> list[list[int]]:
    """
    Given an integer array arr and an integer target, write a function to check if two numbers exist in the array that sum up to the target. If such pairs exist, return all of them, if not return an empty array. You can return the answer in any order.

    You must not return the same pair more than once i.e. all pairs should be unique.

    Input: arr = [1, 2, 2, 3, 4, 5], target = 6
    Output: [[1, 5], [2, 4]]
    Explanation: The numbers 1 and 5, as well as the numbers 2 and 4, sum up to make the target 6.
    """
    arr.sort()
    out = []

    left = 0
    right = len(arr) - 1
    while left < right:
        vals = [arr[left], arr[right]]
        sum = arr[left] + arr[right]

        if sum > target:
            right -= 1
            continue

        elif sum < target:
            left += 1
            continue

        elif sum == target and vals not in out:
            out.append(vals)
        left += 1

    return out


print(duplicate_aware_two_sum([1, 2, 2, 3, 4, 5], 6))
