class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT={}
        window = {}
        res = [-1,-1]
        reslen = float("inf")
        for c in t:
            countT[c] = 1+ countT.get(c,0)
        need = len(countT)
        have = 0
        l = 0
        for r in range(0, len(s)):
            c= s[r]
            window[c] = 1+window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                if (r-l+1) < reslen:
                    res =[l,r]
                    reslen = min(reslen,r-l+1)
                window[s[l]] -=1
                
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have = have -1
                l = l+1
        l,r = res
        return s[l:r+1] if reslen!= float("infinity") else ""



        