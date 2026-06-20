class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        count_fresh = 0
        time = 0
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 1:
                    count_fresh =  count_fresh+1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while count_fresh>0 and q:
            for i in range(0,len(q)):
                r,c = q.popleft()

                for nr,nc in directions:
                    row,col = r+nr,c+nc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        count_fresh = count_fresh -1
            # time is outside for because in que if we have more than one value then 
            # both rot the neighbours simultaneously.
            time +=1
        
        return time if count_fresh == 0 else -1
        