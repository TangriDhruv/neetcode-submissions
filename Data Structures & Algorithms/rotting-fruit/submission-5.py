class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        fresh = 0
        time = 0

        for r in range(0,ROWS):
            for c in range(0,COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh = fresh+1
        
        while q and fresh>0:
            for _ in range(0,len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row + dr, col+dc
                    if (nr<0 or nr>= ROWS or nc<0 or nc>=COLS or grid[nr][nc]!=1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1
            time +=1
        return time if fresh == 0 else -1


        