class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def check(r, c):
            visited = {(r, c)}
            pacific = False
            atlantic = False

            def dfs(r, c):
                nonlocal pacific
                nonlocal atlantic
                nonlocal visited 

                if (r == 0 or c == 0):
                    pacific = True
                if (r == len(heights) - 1 or c == len(heights[0]) - 1):
                    atlantic = True
                if(pacific and atlantic):
                    return True

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr = dr + r 
                    nc = dc + c 

                    if(0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr,nc) not in visited):
                        if(heights[nr][nc] <= heights[r][c]):
                            visited.add((nr, nc))
                            dfs(nr, nc)
                return

            dfs(r,c)

            return pacific and atlantic
        
        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if(check(row, col)):
                    res.append([row,col])
        return res
            