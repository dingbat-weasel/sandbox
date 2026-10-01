# given a string s, write a function that returns true if it is a palindrome
# or false otherwise


def palindrome_checker(s: str) -> bool:
    s_clean = "".join([char for char in s if char.isalnum()]).lower()
    s_list = list(s_clean)

    left: int = 0
    right: int = len(s_list) - 1

    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]

        left += 1
        right -= 1

    return "".join(s_list) == s_clean


class Solution:
    def palindrome_checker(self, s: str) -> bool:
        if not s:
            # An empty string is considered a palindrome
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            char_left = s[left]
            char_right = s[right]

            # Skip non-alphanumeric characters from the left
            if not char_left.isalnum():
                left += 1

            # Skip non-alphanumeric characters from the end
            elif not char_right.isalnum():
                right -= 1

            # Check if the characters are equal ignoring case
            elif char_left.lower() != char_right.lower():
                # Characters are not equal, so it's not a palindrome
                return False

            # Move both pointers towards the center
            else:
                left += 1
                right -= 1

        # All characters have been checked and are equal, so it's a
        # palindrome
        return True
