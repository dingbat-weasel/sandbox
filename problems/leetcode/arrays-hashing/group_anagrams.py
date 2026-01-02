"""
Problem: Group Anagrams
Difficulty: Med
URL: https://neetcode.io/problems/anagram-groups/question?list=neetcode150

Description:
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]

Constraints:

    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.


Approach:
[Explain the approach - what pattern/technique was used?]

Notes:
- [Any insights, edge cases, or gotchas]
- [Alternative approaches considered]
"""

def group_anagrams1(param):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    # solution here
    pass


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        # (input, expected_output),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = group_anagrams1(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
