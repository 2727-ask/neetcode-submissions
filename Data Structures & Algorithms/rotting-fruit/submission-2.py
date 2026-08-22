class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        


        queue = deque([])    
        visited = set()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 2):
                    queue.append((row, col, 0))
                    visited.add((row, col))
                elif(grid[row][col] == 1):
                    fresh = fresh + 1

        
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        mytime = 0
        while queue:
            row, col, time = queue.popleft()

            mytime = time

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc 

                if(0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    visited.add((nr, nc))
                    queue.append((nr, nc, time + 1))
                    fresh = fresh - 1

        if(fresh > 0):
            return -1
        else:
            return mytime




        
        
                    

