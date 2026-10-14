class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 0):
                    queue.append((row, col))

        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if(nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))


        
