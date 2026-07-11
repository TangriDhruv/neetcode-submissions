class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in open_to_close and stack:
                if stack[-1] == open_to_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        