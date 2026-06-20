class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        countS1 = [0]*26
        countS2 = [0]*26
        for c in s1:
            countS1[ord(c)-ord("a")] += 1
        k = len(s1)

        for i in range(0,k):
            countS2[ord(s2[i])-ord("a")] += 1
        if countS1 == countS2:
            return True
        
        for i in range(k,len(s2)):
            countS2[ord(s2[i-k])-ord("a")] -= 1
            countS2[ord(s2[i])-ord("a")] += 1
            if countS1 == countS2:
                return True
        
        return False


                
        