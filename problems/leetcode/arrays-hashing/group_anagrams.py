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

def group_anagrams1(input: list[str]):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    anagrams: dict[int, dict[str, int]] = dict()
    bucket = 0
    out: list[list[str]] = []

    for i, s in enumerate(input):
        # {l1: n, l2:n, l3:n}
        s_hash: dict[str, int] = dict()
        group = []
        for l in s:
            s_hash[l] = s_hash.get(l, 0) + 1

        
        if anagrams[bucket] == s_hash:
            group.append(s)
            out[bucket] = group
        # elif anagrams[bucket] != s_hash:    
        #     anagrams[bucket] = anagrams.get(i, s_hash)
    print(s_hash, anagrams, out)


def group_anagrams2(input: list[str]):
    out = {}

    for s in input:
        # create array of len 26, index = letter, value = count
        count = [0] * 26
        for c in s:
            # ord('a') begins at 97
            count[ord(c) - ord('a')] +=1

        # convert to tuple (lists cant be dict keys)
        key = tuple(count)

        # check if key exists before accessing
        if key not in out:
            out[key] = []

        out[key].append(s)

    return list(out.values())


# generic pattern for grouping
def compute_key(item):
    key = item + 'key'
    return key

def group_generic (items):
    groups = {}
    for item in items:
        key = compute_key(item)

        if key not in groups:
            groups[key] = []
        
        groups[key].append(item)

    


# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
       (["act","pots","tops","cat","stop","hat"], [["hat"],["act", "cat"],["stop", "pots", "tops"]]),
       (["x"], [["x"]]),
       ([""], [[""]]),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = group_anagrams2(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
