class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(0, len(s)):
            curr = ""
            for j in range(i,len(s)):
                curr = curr+s[j]
                #print(curr)
                if curr == curr[::-1]:
                    count = count+1
        
        return count


        