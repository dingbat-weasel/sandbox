"""
Problem: Top K Frequent Elements
Difficulty: Medium
URL: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

Description:
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.


Approach:
- 1st attempt:
    - create a dict for storing seen nums and their counts
    - sort the frequency dict by values desc
    - store and return keys from 0:k

Notes:
- [Any insights, edge cases, or gotchas]
- [Alternative approaches considered]
"""

def top_k_frq_el(nums:list[int], k: int) -> list[int]:
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    freq = {}

    for n in nums: 
        freq[n] = freq.get(n, 0) + 1
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    keys = list(sorted_freq)[:k]

    return keys
    
def top_k_frq_el2(nums: list[int], k: int) -> list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = {}
    freq = [[] for i in range(len(nums) + 1)]    

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res




# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        (([4,5,5,6,6,6], 2), ([5,6], [6, 5])),
        (([7, 7], 1), ([7])),
        (([4, 4, 5, 5, 5, 6, 7, 7, 9, 9], 4), ([5, 7, 9, 4], [4, 5, 7, 9], [5, 4, 7, 9])),
        (([22, 24, 24, 67, 67, 89, 89, 89], 3), ([89, 67, 24], [24,  67, 89], [89, 24, 67])),
    
    ]

    for i, ((nums, k), expected) in enumerate(test_cases):
        result = top_k_frq_el(nums, k)
        status = "✓" if result == expected or result in expected else "✗"
        print(f"Test {i+1}: {status} | Input: {nums}, {k} | Expected one of: {expected} | Got: {result}")
