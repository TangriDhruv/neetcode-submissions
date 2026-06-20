class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res= 0
        l=[]
        for i in range (0,len(tokens)):
            if tokens[i] == '+':
                l.append(l.pop()+l.pop())
            elif tokens[i] == '-':
                a,b = l.pop(),l.pop()
                l.append(b-a)
            elif tokens[i] == '*':
                l.append(l.pop() * l.pop())
            elif tokens[i] == '/':
                a,b = l.pop(),l.pop()
                l.append(int(float(b)/a))
            else:
                l.append(int(tokens[i]))
        return l[0]
