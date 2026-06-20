class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr,open_left,close_left):
            if open_left == 0 and close_left == 0:
                res.append(curr[:])
                return
            if open_left > 0 :
                backtrack(curr+"(",open_left-1,close_left)
            if close_left > open_left:
                backtrack(curr+")",open_left,close_left-1)


        backtrack("",n,n)
        return res
        