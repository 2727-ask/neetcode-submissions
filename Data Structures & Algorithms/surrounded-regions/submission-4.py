class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def dfs(row, col):
            nonlocal visited 
            visited.add((row, col))
            directions = [(0,-1), (0,1), (1,0), (-1,0)]

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col 

                if(0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O" and (nr, nc) not in visited):
                    board[nr][nc] = "T"
                    dfs(nr, nc)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if(row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1):
                    if(board[row][col] == "O"):
                        board[row][col] = "T"
                        dfs(row, col)

        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == "T"):
                    board[row][col] = "O"
                elif(board[row][col] == "O"):
                    board[row][col] = "X"

        

       
        

