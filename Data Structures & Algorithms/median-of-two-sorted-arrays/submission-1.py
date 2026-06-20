class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums) #nlogn        
        
        if len(nums) % 2 == 1:
            mid = len(nums) // 2
            return nums[mid]
        else:
          mid =  len(nums) // 2
          median = (nums[mid] + nums[mid-1]) / 2
          return median