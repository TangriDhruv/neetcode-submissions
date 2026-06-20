class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        print(ub)
        
        while lb <= ub :
            mid = lb +((ub - lb)//2)

            if target > nums[mid] :
                lb = mid+1
            elif target < nums[mid]:
                ub = mid-1 
            else:
                return mid
        return -1
        