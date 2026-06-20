class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        island = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col):
            q = deque()
            grid[row][col] = "0"
            q.append((row,col))

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc  = r+dr,c+dc
                    if (nr < 0 or nc < 0 or nr >= ROW or
                        nc >= COL or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0" 

        
        for r in range(0,ROW):
            for c in range(0,COL):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island += 1
        
        return island


        