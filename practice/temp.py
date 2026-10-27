def pal(test: str) -> bool:
    clean = "".join(char for char in test if char.isalnum()).lower()
    s_list = list(clean)

    left = 0
    right = len(s_list) - 1

    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]

        left += 1
        right -= 1

    return "".join(s_list) == clean
