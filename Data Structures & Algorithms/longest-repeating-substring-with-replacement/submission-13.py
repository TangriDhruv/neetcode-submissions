class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        count = {}
        for r,c in enumerate(s):
            count[c] = count.get(c,0)+1
            while r-l+1 - max(count.values())>k:
                count[s[l]] = count[s[l]]-1
                l = l+1
            max_len = max(max_len,r-l+1)
        return max_len
        