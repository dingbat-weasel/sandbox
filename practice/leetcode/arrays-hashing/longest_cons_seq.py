"""
Problem: Longest consecutive sequence
Difficulty: med
URL: https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150

Description:
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

Constraints:

    0 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9


Approach:
draw values on number line, sequences become obvious
array is made up of several sequences of numbers, looking for the longest
can identify start of sequence by looking at the left neighbor of a number on number line
if theres no left neighbor, no i-1 present in arr, then that number is the first in its sequence, even if len=1
check if i+1 in set for next in sequence
check i+2 etc


if there is left neighbor just continue


Notes:
- use whiteboard to simplify problem, draw spacially.
- can initialize numsSet as set(input param)
- [Alternative approaches considered]
"""


def longest_cons_seq(nums: list[int]):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    numsSet = set(nums)
    longest = 0

    for n in nums:
        # check if start of seq
        if n - 1 not in numsSet:
            length = 0
            while (n + length) in numsSet:
                length += 1
            longest = max(length, longest)
    return longest


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [([2, 20, 4, 10, 3, 4, 5], 4), ([0, 3, 2, 5, 4, 6, 1, 1], 7)]

    for i, (input_data, expected) in enumerate(test_cases):
        result = longest_cons_seq(input_data)
        status = "✓" if result == expected else "✗"
        print(
            f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}"
        )
