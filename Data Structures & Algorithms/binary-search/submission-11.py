class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        lower = 0
        upper = len(nums)-1
        mid = int(lower + (upper-lower)/2)
        def bs(l,u,m):
            if l>u:
                return -1
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                print(l,u,m)
                u = m -1
                m = int(l + (u-l)/2)
                return bs(l,u,m)
            elif nums[m] < target:
                print(l,u,m)
                l = m+1
                m = int(l + (u-l)/2)
                return bs(l,u,m)
            return -1
        
        return bs(lower,upper,mid)



        
            
        