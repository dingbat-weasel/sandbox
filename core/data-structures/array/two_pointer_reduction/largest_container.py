def largest_container(heights: list[int]) -> int:
    out = 0

    i = 0
    j = len(heights) - 1
    while i < j:
        area = min(heights[i], heights[j]) * (j - i)
        out = max(area, out)
        print(area, out, i, j)

        if heights[i] < heights[j]:
            i += 1

        else:
            j -= 1

    return out


print(largest_container([2, 4, 3, 3, 5, 2, 4, 3, 2]))  # 20
