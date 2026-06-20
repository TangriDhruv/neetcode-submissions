class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        lower = 0
        upper = len(nums)-1
        mid = int(lower + (upper-lower)/2)
        print(type(mid))

        while lower <= upper:
            print(mid)
            print(type(mid))
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                lower = mid+1
                mid = int(lower + (upper-lower)/2)
            elif nums[mid]>target:
                upper = mid -1
                mid = int(lower + (upper-lower)/2)
        return -1
        