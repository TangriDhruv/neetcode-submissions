class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def dfs(rows,cols):
            #basecase:
            if (rows == 0 and cols == 0):
                return 1
            elif (rows < 0 or cols < 0):
                return 0
            #Do all stuffs
            right = dfs(rows,cols-1)
            up = dfs(rows-1,cols)
            total = right+up
            return total
        
        return dfs(m-1,n-1)

        