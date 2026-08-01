class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1 :
            return False
        close_to_open = {"]":"[",")":"(","}":"{"}
        stack = []
        for i in range(0,len(s)):
            if stack and s[i] in close_to_open:
                if stack[-1] == close_to_open[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False
