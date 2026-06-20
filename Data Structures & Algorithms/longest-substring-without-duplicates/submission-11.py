class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset ={}
        l = 0
        res = 0

        for r in range(0,len(s)):
            if s[r] in charset:
                print("s[r]: ",s[r])
                temp = charset[s[r]]
                print(temp)
                l = max(l,temp + 1)
                print("l",l)
                charset[s[r]] = r
                print(charset[s[r]])
            charset[s[r]] = r
            print("charset",charset)
            res = max(res,r-l+1)
            print("res",res)

        return res