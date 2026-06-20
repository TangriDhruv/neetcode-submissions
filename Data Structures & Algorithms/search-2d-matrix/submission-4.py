class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row and then find the target
        ROWS = len(matrix)
        COLS = len(matrix[0])-1

        top_row = 0
        bot_row = ROWS-1
        corr_row = -1 

        while top_row <= bot_row:
            corr_row = (top_row + bot_row) // 2
            if target < matrix[corr_row][0]:
                bot_row = corr_row -1
            elif target > matrix[corr_row][COLS]:
                top_row = corr_row+1
            else:
                break
        if not (top_row<=bot_row):
            return False
        print("Corr",corr_row)
        
        l = 0
        r = COLS
        while l<=r:
            mid = l + (r-l)//2
            if target == matrix[corr_row][mid]:
                return True
            elif target < matrix[corr_row][mid]:
                r = mid -1
            else:
                l = mid+1
        return False




        