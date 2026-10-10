class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        matrix = [["."] * n for _ in range(n)]
        print(matrix)
        result = []

        def isSafe(row, col):
            for r in range(row):
                if(matrix[r][col] == "Q"):
                    return False
                
            r = row
            c = col

            while(r >= 0 and c >= 0):
                if(matrix[r][c] == "Q"):
                    return False
                r = r - 1
                c = c - 1

            r = row
            c = col
            
            while(r >=0 and c < n):
                if(matrix[r][c] == "Q"):
                    return False
                r = r - 1
                c = c + 1
            
            return True


        def backtrack(row):
            if(row == n):
                temp = []
                for row in matrix:
                    temp.append("".join(row))
                result.append(temp)
                return

            for col in range(n):
                if(isSafe(row, col)):
                    matrix[row][col] = "Q"
                    backtrack(row + 1)
                    matrix[row][col] = "."

        backtrack(0)
        return result
                
                    

