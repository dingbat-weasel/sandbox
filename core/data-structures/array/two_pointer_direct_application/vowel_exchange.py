# given a string s, write a function to reverse the vowels in the string and return the updated string


def vowel_exchange(s: str) -> str:
    s_list = list(s)
    vowels = ["a", "e", "i", "o", "u"]

    left: int = 0
    right: int = len(s_list) - 1

    while left < right:
        left_char = s_list[left].lower()
        right_char = s_list[right].lower()

        if left_char not in vowels:
            left += 1

        if right_char not in vowels:
            right -= 1

        if left_char in vowels and right_char in vowels:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return "".join(s_list)


class Solution:
    def vowel_exchange(self, s: str) -> str:

        # Create a set to store all the vowels in both uppercase and
        # lowercase
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        # Initialize two pointers, one pointing to the beginning of the
        # string and the other pointing to the end of the string
        left: int = 0
        right: int = len(s) - 1

        # Convert the string to an array for easier manipulation
        chars = list(s)

        # Use a while loop to traverse the string using the two pointers
        while left < right:
            # Check if the character pointed by the first pointer is a
            # vowel. If it is not a vowel, move the pointer to the next
            # character
            if chars[left] not in vowels:
                left += 1

            # Check if the character pointed by the second pointer is a
            # vowel. If it is not a vowel, move the pointer to the
            # previous character
            elif chars[right] not in vowels:
                right -= 1

            # If both pointers point to vowels, swap the characters
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        # Convert the array back to a string and return the modified
        # string
        return "".join(chars)
