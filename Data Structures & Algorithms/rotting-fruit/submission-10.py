class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

      
        

        queue = deque()

        freshFruits = 0
        time = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 2):
                    queue.append((row, col, time))
                elif(grid[row][col] == 1):
                    freshFruits = freshFruits + 1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            row, col, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if(nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    freshFruits = freshFruits - 1
                    queue.append((nr, nc, time + 1))

        if freshFruits == 0:
            return time
        else:
            return -1
                    
            
