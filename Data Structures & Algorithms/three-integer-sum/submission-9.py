class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        res = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            # check first pointer value is same as the previous value
            if (i>0 and nums[i] == nums[i-1]):
                continue
            l,r = i+1,len(nums) -1
            while l < r:
                if nums[i] + nums[l] + nums[r] >0:
                    r = r-1
                elif nums[i] + nums[l] + nums[r] <0:
                    l = l+1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l = l+1
                    r = r-1

                    while nums[l] == nums[l-1] and l<r:
                        l = l+1
                    while nums[r] == nums[r+1] and l<r:
                        r = r-1             
        
        return res

        