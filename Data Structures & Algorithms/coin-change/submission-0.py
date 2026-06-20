class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #create a list to store sub amounts
        #provide a large value of coins to each sub amount
        dp =[amount+1]*(amount+1)
        dp[0] = 0  #0 amount requires 0 coins
        for i in range (1,amount+1): # range is 1-11, values are 1-12 since last value is not included
            for c in coins:
                if (i-c)>=0:
                    dp[i] = min(dp[i],1+dp[i-c]) #added 1 to count the current coin
        return dp[amount] if (dp[amount]!= amount+1) else -1

        