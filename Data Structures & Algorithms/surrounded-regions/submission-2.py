class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for c in range(0,COLS):
            if board[0][c] == "O":
                q.append((0,c))
            if board[ROWS-1][c] == "O":
                q.append((ROWS-1,c))
        
        for r in range(0,ROWS):
            if board[r][0] == "O":
                q.append((r,0))
            if board[r][COLS-1] == "O":
                q.append((r,COLS-1))
        
        while q:
            r,c = q.popleft()
            board[r][c] = "S"
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if (nr <0 or nr >= ROWS or nc<0 or nc >= COLS or board[nr][nc] != "O"):
                    continue
                board[nr][nc] = "S"
                q.append((nr,nc))
        
        for r in range(0,ROWS):
            for c in range(0,COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
            
        

        