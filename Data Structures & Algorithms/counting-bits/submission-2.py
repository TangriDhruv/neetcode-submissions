class Solution:
    def countBits(self, n: int) -> List[int]:
        # create array list that of n+1 length to accomodate 0 at the start
        dp =[0]*(n+1)
        # offset will be used for the repeating patter.
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]
        return dp
        