class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        vis = [[0]*cols for _ in range(rows)]

        count_fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count_fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    vis[r][c] == 2
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while count_fresh > 0 and q:
            for _ in range(0,len(q)):
                r,c = q.popleft()

                for nr,nc in directions:
                    row,col = r+nr,c+nc
                    if (0 <= row < rows and 0 <= col < cols
                        and grid[row][col] == 1 and vis[row][col] == 0):
                        vis[row][col] = 2
                        q.append((row,col))
                        count_fresh -=1
            time = time +1
        if count_fresh ==0:
            return time
        return -1


        