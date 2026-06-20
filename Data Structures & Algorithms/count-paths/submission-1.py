class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #done using BFS graphs.
        q = deque()
        q.append((0,0))
        count = 0
        while q:
            row,col = q.popleft()
            if row == m - 1 and col == n - 1:
                count += 1
                continue
            directions = [(0,1),(1,0)]
            for dr,dc in directions:
                r = row+dr
                c = col+dc
                if (0<=r<m and 0<=c<n):
                    q.append((r,c))
                    
        return count

        