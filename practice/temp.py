def rev(s: str) -> str:

    s_clean = " ".join(s.split())
    words = [word for word in s_clean.split(" ")]

    left = 0
    right = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]

        left += 1
        right -= 1

    return " ".join(words)


print(rev("This   $ is a string    "))
