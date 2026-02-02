"""
Problem: Contains Duplicate
Difficulty: Easy
URL: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

Description:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true


Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

Approach:
use a has set to track seen numbers. for each number, check if its already in the set. If not, add it. leverages O(1) has table lookups

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
- first: for seen = [] if n not in seen requires scanning entire list: O(n), this is done on every element in nums: so O(n^2), slow. also basic logic redundant
- second: set() creates a hash table, unordered unique collection

seen = {} creates an empty dict
for sets use seen = set()

set and dict use hash tables under the hood and allow for index lookup
"""

def has_duplicatev1(nums: list[int]) -> bool:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(?)
    """
    seen = []
    for n in nums:
        if n not in seen:
            seen.append(n)
        elif n in seen:
            return True
        
    return False


def has_duplicate2(nums: list[int]) -> bool:
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
        
    return False



# also O(n) but more concise
# hashes dont contain duplicates, so if duplicates exist
# hash will be shorter length

def has_duplicate3(nums: list[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return bool(len(set(nums)) < len(nums))


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
      ([1, 2, 3, 3], True),        # Has duplicate
      ([1, 2, 3, 4], False),       # No duplicate
      ([1], False),                 # Single element
      ([1, 1], True),              # All duplicates
      ([], False),                  # Empty array
      ([1, 2, 3, 4, 5, 1], True),  # Duplicate at different positions
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = has_duplicate2(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
