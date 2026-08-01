class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #lets try recursion
        dp ={}
        def df(index1,index2):
            if index1 <0:
                return True
            if index2 <0:
                return False
            if (index1,index2) in dp:
                return dp[(index1,index2)]
            
            if s[index1] == t[index2]:
                dp[(index1,index2)] = df(index1-1,index2-1)
                #return df(index1-1,index2-1)
            else:
                #return df(index1,index2-1)
                dp[(index1,index2)]=df(index1,index2-1)
            return dp[(index1,index2)]
        return df(len(s)-1,len(t)-1)
        