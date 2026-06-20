class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # memo =[[float("inf")]*200 for _ in range (0,200)]
        # def dfs(row,col):
        #     if memo[row][col] != float("inf"):
        #             #print(row)
        #         return memo[row][col]
                
        #     elif row >= len(triangle):
        #         return 0
        #     down = dfs(row+1,col)
        #     diag = dfs(row+1,col+1)
        #     print(row)
        #     print(col)
        #     memo[row][col] = min(down,diag)+triangle[row][col]

        #     return memo[row][col]
        # return dfs(0,0)
        m = len(triangle)
        n = len(triangle[-1])
        print(n)
        dp = [[10001]*n for _ in range(0,m)]
        print(dp)
        dp[0][0] = triangle[0][0]
        for i in range (1,m):
            dp [i][0] = dp[i-1][0] + triangle[i][0]
        
        for r in range (1,m):
            for c in range (1,n):
                print('row',r)
                print('col',c)
                if c < len(triangle[r]):
                    dp[r][c] = min(dp[r-1][c-1],dp[r-1][c]) + triangle[r][c]
        print(dp)
        last_row = min(dp[m-1])
        return last_row