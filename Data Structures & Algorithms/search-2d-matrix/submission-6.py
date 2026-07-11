class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while r<len(matrix) and c>=0:
            if target > matrix[r][c]:
                r = r+1
            elif target < matrix[r][c]:
                c = c-1
            else:
                return True
        return False
        