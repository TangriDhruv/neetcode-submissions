class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        l = 0
        max_len = 1

        for r,c in enumerate(s):
            if c in seen and seen[c]>=l:
                l = seen[c] + 1
            seen[c] = r
            max_len = max(max_len,r-l+1)
        return max_len    

        