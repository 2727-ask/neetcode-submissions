class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque([])
        fresh = 0
        curr_time = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 2):
                    queue.append((row,col,0))
                elif(grid[row][col] == 1):
                    fresh = fresh + 1

        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        while(queue):
            row,col,time = queue.popleft()
            curr_time = time
            for dr , dc in directions:
                nr = row + dr 
                nc = col + dc 

                if(0 <= nr < len(grid) 
                and 0 <= nc < len(grid[0]) 
                and grid[nr][nc] == 1):
                    grid[nr][nc] = 2 
                    fresh = fresh - 1
                    queue.append((nr, nc, time + 1))


        if(fresh > 0):
            return -1
        else:
            return curr_time
        



