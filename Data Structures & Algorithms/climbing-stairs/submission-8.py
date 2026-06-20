class Solution:
    def climbStairs(self, n: int) -> int:
        #memoization
        memo = {}
        def dfs(index):
            if index == n:
                return 1
            elif index> n:
                return 0
            elif index in memo:
                return memo[index]
            left = dfs(index+1)
            right = dfs(index+2)
            memo[index] = left+right
            return  memo[index]
        
        return dfs(0)
        
        