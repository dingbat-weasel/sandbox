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
- at first, divide element value from product of whole
- ran into divide by 0 error, if n == 0

- second attempt, handle left and right of n separately and combine
- create two arrays prefix and suffix that track the product of values before and after nums[i]
- combine them for result
- O(3 * n) time, 0(3 * n) memory as well


Notes:
- this one was difficult for me to visualize the code and will revisit
- for divide by 0 errors, handle 0's firsts
- prefix/suffix solution can be optimized for memory, maybe return and try that later

"""

def product_arr_except_self(nums: list[int]) -> list[int]:
    """
    Time Complexity: 
    Space Complexity: 
    """
    product = 1
    out = []
    for n in nums:
        product *= n
    for i, n in enumerate(nums):
        # if prod / n, n==0
        val = (product / n)
        out.append(val)

    return out


def product_arr_except_self2(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(3n)
    Space Complexity: O(3n)
    """
    n = len(nums)
    pref = [0] * n
    suff = [0] * n
    res = [0] * n

    pref[0] = suff[n - 1] = 1
    for i in range(1, n):
        pref[i] = nums[i - 1] * pref[i - 1]

    for i in range(n - 2, -1, -1):
        suff[i] = nums[i + 1] * suff[i + 1]
    
    for i in range(n):
        res[i] = pref[i] * suff[i]
    
    return res

# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ([1,2,4,6],[48,24,12,8]),
        ([-1,0,1,2,3],[0,-6,0,0,0])

    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = product_arr_except_self2(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
