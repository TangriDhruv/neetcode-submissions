class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #lets try dp
        def df(index1,index2):
            if index1 <0:
                return True
            if index2 <0:
                return False
            
            if s[index1] == t[index2]:
                return df(index1-1,index2-1)
            else:
                return df(index1,index2-1)
        return df(len(s)-1,len(t)-1)
        