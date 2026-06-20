class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        #used = [False]*len(nums)

        def backtrack(l):
            if len(l) == len(nums):
                res.append(l[:])
                return
            else:
                for i in range(len(nums)):
                    if nums[i] in l:
                        continue
                    #used[i] = True
                    
                    l.append(nums[i])
                    backtrack(l)
                    l.pop()
                    #used[i] = False
        backtrack([])
        return res

        