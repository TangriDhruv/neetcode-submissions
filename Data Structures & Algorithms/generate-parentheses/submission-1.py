class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def doitagain(current,openleft,closeleft):
            if openleft == 0 and closeleft == 0:
                result.append(current)
                return
            if openleft > 0:
                doitagain(current + "(", openleft-1,closeleft)
            if closeleft > openleft:
                doitagain(current + ")", openleft,closeleft-1)
        doitagain("",n,n)
        return result
