"""
Problem: Two Sum
Difficulty: Easy
URL: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150

Description:
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]

Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]

Constraints:

    2 <= nums.length <= 1000
    -10,000,000 <= nums[i] <= 10,000,000
    -10,000,000 <= target <= 10,000,000
    Only one valid answer exists.


Approach:
[Explain the approach - what pattern/technique was used?]

Notes:
- [Any insights, edge cases, or gotchas]
- [Alternative approaches considered]
"""

def two_sum(input: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    seen = dict()
    for i, val in enumerate(input):
        complement = target - val
        if complement in seen:
            return [seen[complement], i]
        
        seen[val] = i
    return []


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
      (([2, 7, 11, 15], 9), [0, 1]),      # Basic
      (([3, 3], 6), [0, 1]),              # Duplicates
      (([3, 2, 4], 6), [1, 2]),           # Not using same index
      (([-1, -2, -3, -4, -5], -8), [2, 4]),   # Negatives
      (([0, 4, 3, 0], 0), [0, 3]),        # Zeros
  ]

    for i, ((input, target), expected) in enumerate(test_cases):
        result = two_sum(input, target)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input, target} | Expected: {expected} | Got: {result}")
