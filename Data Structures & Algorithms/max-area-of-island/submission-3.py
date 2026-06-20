class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        vis = [[0]*COLS for _ in range(ROWS)]

        def bfs(row,col):
            vis[row][col] = 1
            q = deque()
            q.append((row,col))
            count = 1
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0
                        or vis[nr][nc] == 1):
                        continue
                    else:
                        count = count+1
                        vis[nr][nc] = 1
                        q.append((nr,nc))
            return count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and vis[r][c] == 0:
                    res = max(res,bfs(r,c))
        
        return res
        