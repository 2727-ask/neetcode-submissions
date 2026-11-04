class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        

        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 0):
                    queue.append((row, col))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while(queue):
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = dr + row 
                nc = dc + col 

                if(0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))
       
                    

        
