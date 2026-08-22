class Solution:
    def solve(self, board: List[List[str]]) -> None:


        def dfs(row, col):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            board[row][col] = "T"
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if(0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O"):
                    dfs(nr, nc)
                

        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == "O" and (row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1)):
                    dfs(row, col)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == "O"):
                    board[row][col] = "X"
                elif(board[row][col] == "T"):
                    board[row][col] = "O"

        
