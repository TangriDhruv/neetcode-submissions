class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        index = -1
        while lb <= ub:
            mid = lb + (ub - lb)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lb]:
                if nums[lb] <= target< nums[mid]:
                    ub = mid -1
                else:
                    lb = mid+1
            else:
                if nums[mid] < target <= nums[ub]:
                    lb = mid+1
                else:
                    ub = mid-1
        return -1

        
        