class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add all gates in que and then run bfs don't run bfs on every gate
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        q= deque()

        for r in range(0,ROWS):
            for c in range(0,COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
           
            
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr = dr + row
                nc = dc + col
                if (nr<0 or nr >= ROWS or nc<0 or nc >= COLS or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = grid[row][col]+1
                q.append((nr,nc))