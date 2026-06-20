class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        numset = set(nums)
        for i in numset:
            if i-1 not in numset:
                length = 1
                while (i + length) in numset:
                    length = length + 1
                max_len = max(max_len,length)
        return max_len
        