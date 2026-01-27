"""
Problem: Product of Array Except Self
Difficulty: Medium
URL: https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150

Description:
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

Constraints:

    2 <= nums.length <= 1000
    -20 <= nums[i] <= 20


Approach:
[Explain the approach - what pattern/technique was used?]

Notes:
- hash value at each index
- return product of all values / product[i]

"""

def product_arr_except_self(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    product = 1
    out = []
    for n in nums:
        product *= n
    for i, n in enumerate(nums):
        val = (product / n)
        out.append(val)

    return out
# wip, div by 0



# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ([1,2,4,6],[48,24,12,8]),
        ([-1,0,1,2,3],[0,-6,0,0,0])

    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = product_arr_except_self(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
