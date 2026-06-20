from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n + 1)]

        def backtrack(index, total):
            # base cases
            if total == amount:
                return 1
            if total > amount or index == n:
                return 0
            
            # memoized result
            if memo[index][total] != -1:
                return memo[index][total]
            
            # choice 1: take current coin
            take = backtrack(index, total + coins[index])
            # choice 2: skip current coin
            skip = backtrack(index + 1, total)
            
            # store in memo and return
            memo[index][total] = take + skip
            return memo[index][total]
        
        return backtrack(0, 0)
