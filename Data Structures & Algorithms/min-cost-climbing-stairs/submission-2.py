class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # the cost of reach 1 or second step =0 since you can start from there.
        dp = [0] * (n + 1)

        for i in range(2, n + 1):

            #cost to reach the i th step is the cost to reach till i-1 or i-2 and then the cost you will have to pay at that step.
            #dp[i-1] tell the cost to reach till i-1.
            #cost[i-1] tell the cost you will have to pay at that step to reach ith step.
            # same is with i-2.

            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]