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

Initial attempt was essentially a brute force with many arrays and hash maps to store information
about what has been seen or not, what the board state was. I was spending too much time on this,
so I reviewed the solutions below.

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

true_board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

false_board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def valid_sudoku_initial_unfinished(board):
    """
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    board_map = {}
    row_map = {}
    col_map = {}
    box_map = {}
    for i in range(9):
        box_map[i] = []

    # for each row, add each cell to a seen map coord:digit
    #   0,0 in top left 0-8, 0-8
    # row check: check all digits with same y coord pass tests, i.e. 1-9 unique
    # col check: check all digits with same x coord pass tests
    # box check: x0-2, y0-2 test; x3-5, y0-2 test; x6-8, y0-2 test; etc.

    # map board
    for y, row in enumerate(board):

        for x, value in enumerate(row):
            board_map[(x, y)] = value
            # create row map
            if y in row_map:
                row_map[y].append(value)
            else:
                row_map[y] = [value]

            if x in col_map:
                col_map[x].append(value)
            else:
                col_map[x] = [value]

            if 0 <= x <= 2 and 0 <= y <= 2:
                print("box 0")
                box_map[0].append(value)
            if 3 <= x <= 5 and 0 <= y <= 2:
                box_map[1].append(value)
            if 6 <= x <= 8 and 0 <= y <= 2:
                box_map[2].append(value)
            if 0 <= x <= 8 and 3 <= y <= 5:
                box_map[3].append(value)
            if 3 <= x <= 5 and 3 <= y <= 5:
                box_map[4].append(value)
            if 6 <= x <= 8 and 3 <= y <= 5:
                box_map[5].append(value)
            if 0 <= x <= 2 and 6 <= y <= 8:
                box_map[6].append(value)
            if 3 <= x <= 5 and 6 <= y <= 8:
                box_map[7].append(value)
            if 6 <= x <= 8 and 6 <= y <= 8:
                box_map[8].append(value)
    row_bool = False
    col_bool = False
    box_bool = False

    for row in row_map:
        values = row_map[row]
        row_check = {}
        row_check[row] = [0] * 9
        for value in values:
            if value == ".":
                continue
            if int(value) < 1 or int(value) > 9:
                row_bool = False
            else:
                print(values)
        if len(row_check[row]) > 1:
            row_bool = False
        print(row_check)

    for col in col_map:
        values = col_map[col]
        col_check = {}
        col_check[col] = [0] * 9
        for value in values:
            if value == ".":
                continue
            if int(value) < 1 or int(value) > 9:
                col_bool = False
            else:
                print(values)
        if len(col_check[col]) > 1:
            col_bool = False
        print(col_check)

    return True
    print(row_bool, col_bool, box_bool)
    ans = valid_sudoku(false_board)
    print(ans)


def valid_sudoku_brute(board):
    for row in range(9):
        seen = set()
        for i in range(9):
            if board[row][i] == ".":
                continue
            if board[row][i] in seen:
                return False
            seen.add(board[row][i])

    for col in range(9):
        seen = set()
        for i in range(9):
            if board[i][col] == ".":
                continue
            if board[i][col] in seen:
                return False
            seen.add(board[i][col])

    for square in range(9):
        seen = set()
        for i in range(3):
            for j in range(3):
                row = (square // 3) * 3 + i
                col = (square % 3) * 3 + j
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    print(board[row][col])
                    print(seen)
                    return False
                seen.add(board[row][col])
    return True


from collections import defaultdict


def valid_sudoku_single_pass(board):
    """
    1. Validate the board in a single pass using hash sets:
    rows[r] keeps digits seen in row r
    cols[c] keeps digits seen in col c
    squares[(r // 3, c // 3)] keeps digits in 3x3 box
    2. loop through every cell in board, checks
    3. otherwise add to all three sets
    """
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ),
        (
            [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = valid_sudoku_single_pass(input_data)
        status = "✓" if result == expected else "✗"
        print(
            f"Test {i+1}: {status} | Input: {input_data} | Expected: {expected} | Got: {result}"
        )
