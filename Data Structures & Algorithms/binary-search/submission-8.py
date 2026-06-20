class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1

        while lower<=upper:
            mid = lower+((upper-lower)//2)
            if target>nums[mid]:
                lower = mid + 1
            elif target < nums[mid]:
                upper = mid - 1
            else:
                return mid
        
        return -1
            

        