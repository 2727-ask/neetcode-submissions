class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def dfs(row, col):
            if (row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] != "0"):
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
                return 1
            return 0

        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == "1"):
                    count = count + dfs(row, col)
        
        return count
