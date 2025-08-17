class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                # transpose
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse the rows:
        for row in range(len(matrix)):
            left, right = 0, n - 1
            while left <= right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1




