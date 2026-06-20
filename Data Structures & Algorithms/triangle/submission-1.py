class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo =[[float("inf")]*200 for _ in range (0,200)]
        def dfs(row,col):
            if memo[row][col] != float("inf"):
                    #print(row)
                return memo[row][col]
                
            elif row >= len(triangle):
                return 0
            down = dfs(row+1,col)
            diag = dfs(row+1,col+1)
            print(row)
            print(col)
            memo[row][col] = min(down,diag)+triangle[row][col]

            return memo[row][col]
        return dfs(0,0)
        