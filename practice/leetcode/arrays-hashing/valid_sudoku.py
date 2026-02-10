"""
Problem: Valid Sodoku
Difficulty: Medium
URL: https://leetcode.com/problems/valid-sudoku/description/

Description:

Approach:

given: 9x9 sudoku board
board is valid when:
    - each row contains digits 1-9, no duplicates
    - each column must contain digits 1-9, no duplicates
    - each 3x3 sub-box must contain digits 1-9, no duplicates

board does not have to be full or solveable to be valid

return: true if board is valid, otherwise false

all cells are strings, each row is an array
board is array of 9 arrays.

constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is digit 1-9 or '.'

check for:
    - duplication and in range 1-9 :
        - in each subarray
        - comparing indexes across arrays, for columns
        - in 3x3 sub-boxes.
            - ex: first 3 of subarr 1,2,3
            - index 4,5,6 of subarr 123
            - 789 of sa 123
            - 123 of sa 456
            - 456 of sa 456, etc.

Examples:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true


Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

Notes:
- [Any insights, edge cases, or gotchas]
- [Alternative approaches considered]
"""


def valid_sudoku(board):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    row_check = {}
    col_check = {}
    box_check = {}

    for row in board:
        for cell in row:
            print(cell)


true_board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

valid_sudoku(true_board)

# Test cases
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]],
         True)
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = valid_sudoku(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}")
