class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(i, parity):
            if i == n:
                return 0
            # if we are'nt pickking current num
            ans = dfs(i+1, parity)
            # if we are picking current num
            if parity == 0:
                ans = max(ans, dfs(i+1, parity ^ 1) + nums[i])
            else:
                ans = max(ans, dfs(i+1, parity ^ 1) - nums[i])
            return ans
        return dfs(0, 0)

