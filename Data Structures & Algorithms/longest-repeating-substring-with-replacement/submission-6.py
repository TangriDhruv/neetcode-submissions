class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 1
        seen = {}
        for r in range(0, len(s)):
            seen[s[r]] = seen.get(s[r],0) + 1
            while (r-l+1) - max(seen.values()) >k:
                seen[s[l]] = seen[s[l]] - 1
                l = l+1
            
            max_len = max(max_len,r-l+1)
        return max_len


        