class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range (0,m)]
        dp[0][0] = grid[0][0]
        for r in range(1,m):
            dp[r][0] = dp[r-1][0]+grid[r][0]
        for c in range(1,n):
            dp[0][c] = dp[0][c-1]+grid[0][c]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]

        



            
        