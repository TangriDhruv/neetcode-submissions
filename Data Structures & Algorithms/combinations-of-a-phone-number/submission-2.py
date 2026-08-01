class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs",
         "8":"tuv","9":"wxyz"}

        res =[]

        def backtrack(index,curr):
            if index == len(digits):
                res.append(curr[:])
                return
            for i in mapping[digits[index]]:
                print(i)
                backtrack(index+1,curr+i)
        backtrack(0,"")
        return res
