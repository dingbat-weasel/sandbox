"""
Problem: Valid Anagram
Difficulty: Easy
URL: https://neetcode.io/problems/is-anagram/question?list=neetcode150

Description:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

Constraints:

    s and t consist of lowercase English letters.


Approach:
1,2. two hash maps, optimal time, requires extra space
3. Counter(s) == Counter(t)
4. sorting


Notes:
- Counter from collections is built for this purpose
- 5: count up with str1 and then decrement using str2 to find differences with a single hashmap
"""

def valid_anagram1(s: str, t: str):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s) != len(t):
        return False
    
    s_hash: dict[str, int] = dict()
    t_hash: dict[str, int] = dict()

    for l in s:
        if l not in s_hash:
            s_hash.__setitem__(l, 0)
        val = s_hash[l]
        val += 1
        s_hash[l] = val

    for k in t:
        if k not in t_hash:
            t_hash.__setitem__(k, 0)
        val = t_hash[k]
        val += 1
        t_hash[k] = val

    if s_hash == t_hash:
        print(s_hash, t_hash)
        return True
    
    print(s_hash, t_hash)
    return False

def valid_anagram2(s: str, t: str):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s) != len(t):
        return False
    
    s_hash: dict[str, int] = dict()
    t_hash: dict[str, int] = dict()

    # other method for incrementing
    for l in s:
        s_hash[l] = s_hash.get(l, 0) + 1

    for k in t:
        t_hash[k] = t_hash.get(l, 0) + 1

    if s_hash == t_hash:
        return True
    
    return False

from collections import Counter
def valid_anagram3(s: str, t: str):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return Counter(s) == Counter(t)

# other approaches
def valid_anagram4(s: str, t: str):
    """
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n)
    """
    return sorted(s) == sorted(t)

def valid_anagram5(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}

    # Increment for s
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Decrement for t
    for char in t:
        counts[char] = counts.get(char, 0) - 1
        if counts[char] < 0:  # Found char in t not in s
            return False

    return all(count == 0 for count in counts.values())

# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
      # Basic valid anagrams
      (("anagram", "nagaram"), True),
      (("listen", "silent"), True),
      (("abc", "bca"), True),

      (("rat", "car"), False),
      (("hello", "world"), False),

      (("aaa", "aa"), False),
      (("abc", "abcc"), False),

      (("", ""), True),
      (("a", "a"), True),
      (("a", "b"), False),
      (("abc", "abcd"), False),

      (("aacc", "ccac"), False),
      (("ab", "a"), False),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = valid_anagram5(input_data[0], input_data[1])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
