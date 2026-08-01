class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(l):
            if len(l) == len(nums):
                res.append(l[:])
                return
            
            for i in range(0,len(nums)):
                if nums[i] in l:
                    continue
                l.append(nums[i])
                backtrack(l)
                l.pop()
        backtrack([])
        return res
        