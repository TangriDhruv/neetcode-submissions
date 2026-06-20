class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        u = len(nums)-1

        while l <= u:
            if nums[l] < nums[u]:
                res = min(res, nums[l])
                break
            mid = l + (u-l)//2
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                u = mid-1
        return res
        