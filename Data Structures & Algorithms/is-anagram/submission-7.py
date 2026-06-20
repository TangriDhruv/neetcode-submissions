class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0]*26
        t1 = [0]*26
        for c in s:
            s1[(ord(c)-ord("a"))] +=1
        for c in t:
            t1[(ord(c)-ord("a"))] +=1
        return s1 == t1
        