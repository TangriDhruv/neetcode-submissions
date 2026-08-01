class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb = 0
        ub = len(nums)-1
        minimum = float("inf")

        while lb<=ub:
            mid = lb + (ub-lb) //2
            if nums[lb] <= nums[mid]:
                minimum = min(minimum,nums[lb])
                lb = mid+1
            else:
                minimum = min(minimum,nums[mid])
                ub = mid-1
        return minimum 



        