class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int, i: int) -> bool:
            # matched all chars
            if i == len(word):
                return True

            # invalid cell or mismatch
            if (r < 0 or r >= row or c < 0 or c >= col or
                visited[r][c] or board[r][c] != word[i]):
                return False

            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True

            visited[r][c] = False  # backtrack
            return False

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
