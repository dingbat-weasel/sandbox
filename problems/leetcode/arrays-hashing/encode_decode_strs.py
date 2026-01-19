"""
Problem: Encode and Decode Strings
Difficulty: Medium
URL: https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

Description:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}

So Machine 1 does:

string encoded_string = encode(strs);

and Machine 2 does:

vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:

Input: dummy_input = [""]

Output: [""]


Constraints:

    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.


Follow up: Could you write a generalized algorithm to work on any possible set of characters?

Approach:
[Explain the approach - what pattern/technique was used?]

Notes:
- [Any insights, edge cases, or gotchas]
- [Alternative approaches considered]
"""

def encode_decode_strs1(strs: list[str]):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    def encoder(strs: list[str]) -> str:
        encoded_str = ' '.join(strs)

        return encoded_str
    
    network_state = encoder(strs)

    def decoder(str: str) -> list[str]:
        decoded_str = str.split(' ')

        return decoded_str

    message = decoder(network_state)
    return message

def encode_decode_strs2(strs: list[str]):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    def encoder(strs: list[str]) -> str:
        encoded_str = ""
        for s in strs:
            delim = str(len(s)) + '#'
            encoded_str += delim + s
            

        print(encoded_str)

        return encoded_str
    
    network_state = encoder(strs)

    def decoder(str: str) -> list[str]:
        decoded_str, i = [], 0

        while i < len(str):
            j = i
            while [j] != '#':
                j += 1
            length = int(str[i:j])
            decoded_str.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_str
    
    # debug this next time
            

    message = decoder(network_state)
    return message

# Test cases
if __name__ == "__main__":
    test_cases = [
        (["Hello", "world"], ["Hello", "world"]),
        (["Message", "plenty received"], ["Message", "plenty received"]),
        (['Oops', '#mistake', 'test'], ['Oops', '#mistake', 'test']),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = encode_decode_strs2(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
