class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # STEP 1: Find the right shelf
        top = 0
        bottom = len(matrix) - 1
        
        while top <= bottom:
            row = (top + bottom) // 2
            start = matrix[row][0]
            end = matrix[row][-1]
            
            if target > end:
                # Target is bigger than the whole shelf, move down
                top = row + 1
            elif target < start:
                # Target is smaller than the whole shelf, move up
                bottom = row - 1
            else:
                # We found the shelf! (start <= target <= end)
                # STEP 2: Use your exact Binary Search code on this row
                
                left = 0
                right = len(matrix[row]) - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    
                    if matrix[row][mid] == target:
                        return True 
                    elif matrix[row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
                # If we searched the shelf and didn't find it
                return False
                
        # If we looked at all shelves and it's not anywhere
        return False