class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums = nums1 + nums2
        nums = sorted(nums) # nlogn
        mid = 0 + (len(nums)-0)//2
        median = -1
        if len(nums)%2 == 0:
            median = (nums[mid -1] + nums[mid])/2
        else:
            median = nums[mid]
        
        return median

