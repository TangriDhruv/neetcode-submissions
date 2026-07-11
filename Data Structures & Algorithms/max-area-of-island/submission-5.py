class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            count = 1

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = row+dr
                    nc = col+dc
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc] == 0):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    count = count+1
            return count
                    

        
        for r in range(0,ROWS):
            for c in range(0,COLS):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    max_area = max(max_area,area)
        
        return max_area
        