"""
Generally easy  problems; if it follows the template below it can be solved by applying the two-pointer technique directly.

Template:
    Given an arr perform some operations on arr[i] and arr[j] such that i<j and with each iteration, i and j move closer to each other by some steps

    Both i and j may start from some arbitrary indeces x and y in the arr such that x<y

Example problems:
    - flip characters
    - palindrome checker
    - vowel exchange
    - reverse words
    - reverse segments
    - reverse word order
"""


def reverse_brute(arr: list[str]) -> None:
    """
    Requires two traversals and additional space for temp arr.
    """
    # create temp arr to store reverse
    temp: list[str] = ["" for _ in range(len(arr))]

    last_index = len(arr) - 1

    # traverse arr in reverse direction and copy to temp
    for i in range(last_index, -1, -1):
        temp[last_index - 1] = arr[i]

    # copy temp back to arr
    for i in range(last_index + 1):
        arr[i] = temp[i]


def reverse_tp(arr: list[str]) -> None:
    """
    template: given an arr (arr) perform some operations (swap) on arr[i] and arr[j] such that i<j and with each iteration, i and j move closer to each other by some steps (1 step each).

    both i and j may start from some arbitrary indices x (0) and y (arr.length - 1) in the arr such that x<y.
    """

    # initialize the two pointers, one pointing to the beginning of the
    # array and the other pointing to the end of the array
    left: int = 0
    right: int = len(arr) - 1

    # use a while loop to traverse the arr using the two pointers
    while left < right:
        # swap the values pointed by the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]

        # move the pointers towards the center of the arr
        left += 1
        right -= 1
