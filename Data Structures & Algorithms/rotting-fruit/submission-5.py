class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque([])
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 2):
                    queue.append((row, col, 0))
                    visited.add((row, col))
                if(grid[row][col] == 1):
                    fresh = fresh + 1
        
        if(fresh == 0):
            return 0

        directions = [(0,1), (0,-1), (1,0), (-1, 0)] 
        time = 0
        while(queue and fresh):
            row, col, minute = queue.popleft()
            time = minute
            for dr, dc in directions:
                nr = dr + row 
                nc = dc + col 

                if(0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == 1):
                    grid[nr][nc] = 2 
                    fresh = fresh - 1
                    visited.add((nr,nc))
                    queue.append((nr, nc, minute + 1))
        return time+1 if fresh == 0 else -1

        
