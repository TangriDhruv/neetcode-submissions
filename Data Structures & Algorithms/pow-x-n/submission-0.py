class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n >= 0:
            for i in range (0,n):
                ans = ans*x
            return ans
        elif n<0:
            for i in range(0,abs(n)):
                ans = ans*x
            return float(1/ans)
