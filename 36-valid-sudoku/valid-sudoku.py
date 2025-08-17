class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashmap = {i: set() for i in range(9)}
        col_hashmap = {i: set() for i in range(9)}
        square_hashmap = {}

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                index = (row//3, col//3)
                if index not in square_hashmap:
                    square_hashmap[index] = set()
                if board[row][col] in row_hashmap[row] or board[row][col] in col_hashmap[col] or board[row][col] in square_hashmap[index]:
                    return False
                else:
                    row_hashmap[row].add(board[row][col])
                    col_hashmap[col].add(board[row][col])
                    square_hashmap[index].add(board[row][col])

        return True