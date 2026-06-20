class Solution:
    def isValid(self, s: str) -> bool:
        if (s == ''):
            return False
        stack = []
        for c in s:
            print(c)
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
                print(stack)
            else:
                if not stack:
                    return False

                top = stack[-1]
                if (c == '}' and top == '{') or (c == ')' and top == '(') or (c == ']' and top == '['):
                    stack.pop()
                else:
                    return False
        return True if not stack else False