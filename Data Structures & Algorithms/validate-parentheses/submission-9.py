class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_par = {")":"(", "}":"{","]":"["}
        for par in s:
            if par in valid_par :
                if stack and stack[-1] == valid_par[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return not stack
        

        