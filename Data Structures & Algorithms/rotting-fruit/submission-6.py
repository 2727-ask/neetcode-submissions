class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ans = 0
        while queue:
            row, col, count = queue.popleft()
            ans = count
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if(nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 1):
                    grid[nr][nc] = -1
                    queue.append((nr, nc, count + 1))

        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 1):
                    return -1
        
        return ans