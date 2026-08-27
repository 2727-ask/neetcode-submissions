class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

       
        def check(r, c):
            visited = {(r,c)}
            pacific = False
            atlantic = False 

            def dfs(row, col):
                nonlocal pacific 
                nonlocal atlantic
                nonlocal visited

                directions = [(0,1), (0,-1), (1,0), (-1, 0)]

                if(row == 0 or col == 0):
                    pacific = True 
                if(row == len(heights) - 1 or col == len(heights[0]) - 1):
                    atlantic = True 
                
                if(pacific and atlantic):
                    return True

                for dr, dc in directions:
                    nr = dr + row 
                    nc = dc + col 

                    if(0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr, nc) not in visited):
                        if(heights[nr][nc] <= heights[row][col]):
                            visited.add((nr, nc))
                            dfs(nr, nc)
                            
                return False
            dfs(r,c)
            return pacific and atlantic


        result = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if(check(row,col) == True):
                    result.append([row,col])

        return result

                