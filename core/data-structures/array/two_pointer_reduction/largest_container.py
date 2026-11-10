def largest_container(heights: list[int]) -> int:
    """
    You are given an integer array heights, where heights[i] represents the height of a wall at position i. Write a function to find two walls that, together with the x-axis, form a container holding the maximum water and return the area of this container.

    Area = min(heights[i], heights[j]) * (j - i)
    Where i and j are the indices of the two walls, and i < j.

    It is guaranteed that the input array will always contain more than one element.

    Input: heights = [2, 4, 3, 3, 5, 2, 4, 3, 2]
    Output: 20
    Explanation: In the above heights array (represented by grey colour), the area of the container with the most water is 20 (represented by green).
    """
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
