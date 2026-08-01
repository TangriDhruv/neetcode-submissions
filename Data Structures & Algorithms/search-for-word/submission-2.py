class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(row,col,index):

            if index == len(word): 
                return True
            if (row<0 or row>=ROWS or col < 0 or col>=COLS or (row,col) in visited or board[row][col] != word[index]):
                return False
            visited.add((row,col))
            
            res = (dfs(row+1,col,index+1) or
                  dfs(row-1,col,index+1) or
                  dfs(row,col+1,index+1) or
                  dfs(row,col-1,index+1))
            visited.remove((row,col))
            return res



        
        for r in range(0,ROWS):
            for c in range(0,COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False
        
        