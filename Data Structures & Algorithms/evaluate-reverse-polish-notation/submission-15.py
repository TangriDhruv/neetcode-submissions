class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if stack and t in "+-*/":
                first = stack.pop()
                second = stack.pop()
                if t == "+":
                    ans = int(first) + int(second)
                    stack.append(ans)
                elif t == "-":
                    ans = int(second) - int(first)
                    stack.append(ans)
                elif t == "*":
                    ans = int(first) * int(second)
                    stack.append(ans)
                else:
                    ans = int(second)/int(first)
                    stack.append(ans)
            else:
                stack.append(t)
        return int(stack[-1])



        