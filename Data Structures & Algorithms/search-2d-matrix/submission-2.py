class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows = len(matrix)
        Cols = len(matrix[0])
        top_row = 0
        bot_row = Rows-1
        mid_row = (top_row + bot_row) // 2
        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            elif target == matrix[mid_row][0]:
                return True
            elif target == matrix[mid_row][-1]:
                return True
            elif matrix[mid_row][0] < target < matrix[mid_row][-1]:
                break
        
        first_col = 0
        last_col = Cols-1
        while first_col <= last_col:
            mid_col = ((first_col + last_col)//2)
            if target > matrix[mid_row][mid_col]:
                first_col = mid_col + 1
            elif target < matrix[mid_row][mid_col]:
                last_col = mid_col - 1
            elif target == matrix[mid_row][mid_col]:
                return True
        
        return False




        