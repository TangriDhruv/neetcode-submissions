class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}

        for i in range(0,len(nums)):
            d[nums[i]] = d.get(nums[i],0) + 1

        for i,j in d.items():
            if d[i] == 1:
                return i
        return 0
        