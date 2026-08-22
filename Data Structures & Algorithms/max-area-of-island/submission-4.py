class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(row, col):
            if(0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0):
                grid[row][col] = 0
                return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
            else:
                return 0

        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 1):
                    area = max(area, dfs(row, col))
        return area