class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        def capture(row, col):
            if(0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] != "X" and board[row][col] != "T"):
                board[row][col] = "T"

                capture(row + 1, col)
                capture(row - 1, col)
                capture(row, col + 1)
                capture(row, col - 1)
            return



        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] != "X" and (row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1)):
                    capture(row, col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == "T"):
                    board[row][col] = "O"
                elif(board[row][col] == "O"):
                    board[row][col] = "X"
