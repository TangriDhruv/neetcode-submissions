class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False]*len(nums)
        
        def backtrack(l):
            if len(l) == len(nums):
                res.append(l[:])
                return
            for i in range(0,len(nums)):
                if used[i]:
                    continue
                if (i>0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                l.append(nums[i])
                used[i] = True
                backtrack(l)
                l.pop()
                used[i] = False
        backtrack([])
        return res
        