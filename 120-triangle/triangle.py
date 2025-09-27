class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]                 # copy last row
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
        return dp[0]


        