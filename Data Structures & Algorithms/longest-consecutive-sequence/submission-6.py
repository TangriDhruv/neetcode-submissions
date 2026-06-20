class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        print(numset)
        length = 0
        max_len = 0

        for num in numset:
         
            if num - 1 not in numset:
           
                length = 1
                while num + length in numset:
                    length = length+1
                max_len = max(max_len,length)
        return max_len
        