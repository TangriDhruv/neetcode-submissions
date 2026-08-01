class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(index):
            if index < 0:
                return 0
            if index == 0:
                return 1
            if index in memo:
                return memo[index]
            left = dfs(index-1)
            right = dfs(index-2)
            memo[index] = left+right
            return memo[index]
        
        return dfs(n)
        