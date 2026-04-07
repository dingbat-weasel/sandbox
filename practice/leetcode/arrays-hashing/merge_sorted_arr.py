"""
Problem: [merge sorted arr]
Difficulty: [Easy/Medium/Hard]
URL: [https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/]

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Approach:
- two arrays, sorting the second into the first
- could have no elements in one or either
- one approach:
    loop over nums1, loop over nums2 and insert based on value


Notes:
- [Any insights, edge cases, or gotchas]
- [Alternative approaches considered]
"""

def merge_sorted(nums1: list[int], m, nums2: list[int], n):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """

    if n == 0:
        return nums1
    if m == 0:
        nums1[m:] = nums2
        return nums1

    k = 0
    while k < n:
        for i, num in enumerate(nums1):
            print(k)
            if nums2[k] <= num:
                nums1.insert(i, nums2[k])
                k += 1
            if i == m:
                nums1[m:] = nums2[k:]
                break
    return nums1


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        (([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6]),
        (([1], 1, [], 0), [1]),
        (([0], 0, [1], 1), [1]),
    ]

    for i, ((n1, m, n2, n), expected) in enumerate(test_cases):
        result = merge_sorted(n1, m, n2, n)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {n1, m, n2, n} | Expected: {expected} | Got: {result}")
