class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque([])
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 0):
                    queue.append((row, col, 1))
                    visited.add((row,col))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            row, col, dist = queue.popleft()
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col 
                if(0 <= nr < len(grid) and (0 <= nc < len(grid[0])) and grid[nr][nc] != -1 and (nr,nc) not in visited):
                    grid[nr][nc] = dist
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist+1))
        

