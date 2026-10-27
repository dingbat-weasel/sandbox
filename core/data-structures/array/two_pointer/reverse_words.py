# Given a string s, write a function that reverses the characters of each word
# in the given string while preserving the original word order.
# The string may contain leading or trailing spaces,
# and the words in the input string might be separated by more than a single space character.

# All spaces, including consecutive spaces, must be preserved exactly as in the input.


class Solution:
    def find_word_end(self, arr: list[str], start: int) -> int:

        end = start
        while end < len(arr) and arr[end] != " ":
            end += 1

        return end - 1

    def reverse_word(self, arr: list[str], start: int, end: int) -> None:
        left = start
        right = end

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

    def reverse_words(self, s: str) -> str:
        arr = list(s)
        start = 0

        # iterate through the string
        while start < len(arr):
            # skip leading spaces
            if arr[start] == " ":
                start = start + 1
                continue

            # place the end pointer at the end of the word
            end = self.find_word_end(arr, start)

            # reverse word
            self.reverse_word(arr, start, end)

            # place start at beginning of next word
            start = end + 1

        return "".join(arr)
