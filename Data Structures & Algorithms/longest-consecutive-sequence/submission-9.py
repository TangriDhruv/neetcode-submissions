class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        max_len = 0
        num_set = set(nums)

        for nums in num_set:
            if nums - 1 not in num_set:
                longest = 1
                while nums + longest in num_set:
                    longest = longest+1
                max_len = max(max_len,longest)
        return max_len
            
            
        