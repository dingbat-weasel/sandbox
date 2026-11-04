def reverse_word_order(s: str) -> str:
    """
    Reverse word order

    Given a string s, write a function that returns a new string with the words of the original string in reverse order separated by a single space. The returned string must contain no leading or trailing spaces and only one space between each word.

    Words in the input are separated by one or more spaces, and the string may contain leading, trailing, or multiple spaces between words.

    Input: s = "This is a string"
    Output: "string a is This"
    Explanation: All the words of the given string are concatenated in reverse order and separated by a single space.
    """
    cleaned = " ".join(s.split())
    words = [word for word in cleaned.split(" ")]

    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right].strip(), words[left].strip()

        left += 1
        right -= 1

    return " ".join(words)


print(reverse_word_order("  This  is a     string"))
