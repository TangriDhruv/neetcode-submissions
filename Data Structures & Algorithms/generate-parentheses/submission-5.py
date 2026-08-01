class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(curr,open_bracket,close_bracket):
            if open_bracket == 0 and close_bracket == 0:
                res.append(curr)
                return
            if open_bracket >0:
                backtrack(curr+"(",open_bracket-1,close_bracket)
            if close_bracket>open_bracket:
                backtrack(curr+")",open_bracket,close_bracket-1)
        backtrack("",n,n)
        return res
        