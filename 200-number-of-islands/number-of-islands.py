class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def erase(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            erase(i+1, j); erase(i-1, j); erase(i, j+1); erase(i, j-1)

        i = 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] == "1":
                    count += 1
                    erase(i, j)           # erase it island so we do not recount it
                j += 1
            i += 1
        return count