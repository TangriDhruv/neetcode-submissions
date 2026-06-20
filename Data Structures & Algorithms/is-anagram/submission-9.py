class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_s = [0]*26
        

        for i in range(len(s)):
            arr_s[(ord(s[i]) - (ord("a")))] +=1
        
        for i in range(len(t)):
            arr_s[(ord(t[i]) - (ord("a")))] -=1
        
        for i in range(0, len(arr_s)):
            if arr_s[i] != 0:
                return False
        return True


        