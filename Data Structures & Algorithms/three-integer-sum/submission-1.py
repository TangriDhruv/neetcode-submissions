class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for index,val in enumerate(nums):
            if index >0 and nums[index-1] == val:
                continue

            l,r = index+1,len(nums)-1
            while l<r:
                threesum = val+nums[l]+nums[r]
                if threesum>0:
                    r = r-1
                elif threesum<0:
                    l = l+1
                else:
                    res.append([val,nums[l],nums[r]])
                    l=l+1
                    r= r-1
                    while nums[l] == nums[l-1] and l <r:
                        l =l+1
        return res
        