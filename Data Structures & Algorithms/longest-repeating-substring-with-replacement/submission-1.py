class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter = {}
        res = 0
        l = 0
        mxf = 0
        for r in range (len(s)):
            if s[r] in letter.keys():
                letter[s[r]] = letter[s[r]]+1
            else:
                letter[s[r]] = 1
            mxf = max(mxf,letter[s[r]]) # this will check current character count and max value

            while (r-l+1)-mxf > k:
                letter[s[l]]= letter[s[l]]- 1
                l=l+1
            res = max(res, r-l+1)
        
        return res
        