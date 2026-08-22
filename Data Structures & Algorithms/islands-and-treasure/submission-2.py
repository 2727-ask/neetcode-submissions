class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque([])
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 0):
                    queue.append((row, col, 1))


        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while(queue):
            row, col, dist = queue.popleft()
            for dr, dc in directions:
                nr = row + dr 
                nc = col + dc

                if(0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and ((nr,nc) not in visited) and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = dist
                    queue.append((nr, nc, dist + 1))
        







