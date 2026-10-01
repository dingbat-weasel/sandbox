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
