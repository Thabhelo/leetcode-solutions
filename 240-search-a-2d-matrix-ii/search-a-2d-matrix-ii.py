class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True  # Target found
        # return False 

        numRows, numCols = len(matrix), len(matrix[0])
        row, col = numRows - 1, 0  # Start from the bottom-right corner
        
        while row >= 0 and col < numCols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1  # Move left
            else:
                col += 1  # Move down
        
        return False  # Target not found