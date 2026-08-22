class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        visited = set()
        print(adjList)
        res = 0
        def dfs(i):
            nonlocal res
            visited.add(i)
            for child in adjList[i]:
                if(child not in visited):
                    dfs(child)
        
        for key, val in adjList.items():
            if(key not in visited):
                dfs(key)
                res = res + 1
                
        
        return res
            

        