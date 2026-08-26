class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if(0 > row or row >= len(grid) or 0 > col or col >= len(grid[0]) or grid[row][col] == "0"):
                return

            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
                
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == "1"):
                    dfs(row, col)
                    count = count + 1
        
        return count

        