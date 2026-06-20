class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        row = len(heights)
        col = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r,c,vis,prevheight):
            if ((r,c) in vis or r<0 or c<0 or r == row or c == col
                or heights[r][c] < prevheight):
                return
            vis.add((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (0<= new_r < row and 0<= new_c < col
                    and (new_r,new_c) not in vis and heights[new_r][new_c] >= prevheight):
                    dfs(new_r,new_c,vis,heights[new_r][new_c])

        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])

        

        for r in range(row):
            for c in range(col):
                if ((r,c) in atl and (r,c) in pac):
                    res.append([r,c])
        return res

            

        