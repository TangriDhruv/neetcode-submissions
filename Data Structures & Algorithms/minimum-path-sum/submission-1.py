class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1]*n for _ in range (0,m)]
        print(memo)
        def dfs(row,col):
            if row == 0 and col == 0:
                return grid[row][col]
            elif row < 0 or col <0:
                return float("inf")
            elif memo[row][col] != -1:
                return memo[row][col]
            left = dfs(row,col-1)
            up = dfs(row-1,col)
            memo[row][col] = min(left,up)+grid[row][col]
            return memo[row][col]
        return dfs(m-1,n-1)


            
        