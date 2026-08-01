class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Three cases:
        #1. All positive sum them all
        #2. Evene -ves sum them all
        #3. Odd -ves (prefix before -ve and suffix after -ve)
        #4. Could have 0's (divide the array to before and sfter that zero)
        prefix = 1
        suffix = 1
        n = len(nums)
        max_prod = float("-inf")

        for i in range(0, n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]
            max_prod = max(max_prod,max(prefix,suffix))
        
        return max_prod

        