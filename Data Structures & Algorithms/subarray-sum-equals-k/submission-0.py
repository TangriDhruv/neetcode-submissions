class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create a map of prefix sum and count (how many time that prefix sum appears)
        # manage a currSum variable
        currSum = 0
        prefix = {0:1}
        res = 0
        for n in nums:
            currSum = currSum+n
            diff = currSum-k
            res += prefix.get(diff,0)
            prefix[currSum] = 1+ prefix.get(currSum,0)
        return res
        
        
        