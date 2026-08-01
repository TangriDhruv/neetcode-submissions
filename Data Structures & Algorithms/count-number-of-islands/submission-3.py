class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island = 0

        def dfs(row,col):
            if (row<0 or row>= ROWS or col<0 or col>=COLS or grid[row][col] != "1"):
                return
            grid[row][col] = 0
            dfs(row+1,col)
            dfs(row-1,col) 
            dfs(row,col+1) 
            dfs(row,col-1)


        for r in range(0,ROWS):
            for c in range(0,COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island = island+1
        return island
        