class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                val = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif t == "-":
                val = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif t == "*":
                val = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif t == "/" :
                if stack[-2]!=0:
                    val = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                else:
                    stack.pop()
                    stack.pop()
                    stack.append(0)
            else:
                stack.append(int(t))
        return stack[-1]
            

