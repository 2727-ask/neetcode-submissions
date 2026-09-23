class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rowset = set()
        colset = set()

            

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == 0):
                    rowset.add(row)
                    colset.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(row in rowset or col in colset):
                    matrix[row][col] = 0
                
                    
        
                