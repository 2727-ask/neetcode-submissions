class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []

        def check(row, col):
            visited = set()
            directions = [(0,1), (0,-1), (1, 0), (-1,0)]
            visited.add((row, col))
            pacific = False
            atlantic = False

            def dfs(row, col):
                nonlocal atlantic 
                nonlocal visited
                nonlocal directions
                nonlocal pacific
                visited.add((row, col))

                if(row == 0 or col == 0):
                    pacific = True
                if(row == len(heights) - 1 or col == len(heights[0]) - 1):
                    atlantic = True
                
                if pacific and atlantic:
                    return
                
                for dr, dc in directions:
                    nr = row + dr 
                    nc = col + dc

                    if(0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr, nc) not in visited):
                        if(heights[row][col] >= heights[nr][nc]):
                            dfs(nr, nc)

            dfs(row, col)
            return pacific and atlantic



        output = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if(check(row, col)):
                    output.append([row, col])
        return output

                