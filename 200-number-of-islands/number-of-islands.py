class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            dfs(i + 1, j) # bottom
            dfs(i, j + 1) # right
            dfs(i - 1, j) # top
            dfs(i, j - 1) # left

        number_of_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                number_of_islands += 1
                dfs(i, j)
                
        return number_of_islands
