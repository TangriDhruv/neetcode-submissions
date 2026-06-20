class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def dfs(row,col):
            visited[row][col] = 1
            count = 1
            direction = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in direction:
                new_r = row+dr
                new_c = col+dc
                if (0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and visited[new_r][new_c] == 0 
                    and grid[new_r][new_c] == 1):
                    
                    count += dfs(new_r,new_c)
            return count

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    
                    area = dfs(r,c)
                    result = max(result,area)
        return result