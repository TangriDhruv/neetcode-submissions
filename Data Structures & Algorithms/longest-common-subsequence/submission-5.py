class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(index1,index2):
            if index1 < 0 or index2 < 0:
                return 0
            if (index1,index2) in memo:
                return memo[(index1,index2)]
            if text1[index1] == text2[index2]:
                memo[(index1,index2)] = 1 + dfs(index1-1,index2-1) 
            if text1[index1] != text2[index2]:
                memo[(index1,index2)]= 0 + max(dfs(index1-1,index2), dfs(index1,index2-1))
            return memo[(index1,index2)]
        return dfs(len(text1)-1,len(text2)-1)
            
        