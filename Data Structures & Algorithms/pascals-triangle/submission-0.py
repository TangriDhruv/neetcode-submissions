class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0]*numRows for _ in range(0,numRows)]
        res = []
        for r in range(numRows):
            dp[r][0] = 1
        
        for r in range(1,numRows):
            for c in range(1,numRows):
                dp[r][c] = dp[r-1][c-1] + dp[r-1][c]
        
        for r in range(0,numRows):
            l = []
            for c in range(0,numRows):
                if dp[r][c] != 0:
                    l.append(dp[r][c])
            res.append(l)
        return res


        