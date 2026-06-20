class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result =[]
        def backtrack (index,curr):
            if index == len(s):
                result.append(curr[:])
                return
            for i in range(index,len(s)):
                substring = s[index:i+1]
                if ispalindrome(substring):
                    curr.append(substring)
                    backtrack(i + 1, curr)
                    curr.pop()
        
        def ispalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
            
        backtrack(0,[])
        return result
        