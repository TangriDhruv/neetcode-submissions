class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_len = 0

        for num in numset:
            # only start counting if it's the beginning of a sequence
            if num - 1 not in numset:
                current = num
                length = 1

                while current + 1 in numset:
                    current += 1
                    length += 1

                max_len = max(max_len, length)

        return max_len

        