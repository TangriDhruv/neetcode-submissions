class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for i in range(0,len(nums)):
            print(nums[i])
            if nums[i] == 1:
                count = count + 1
            else:
                res = max(res,count)
                count = 0
        res = max(res,count)
        return res
        