class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}


        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        visited = set()

        def dfs(i):
            visited.add(i)
            for x in adjList[i]:
                if(x not in visited):
                    dfs(x)

        res = 0
        for key, val in adjList.items():
            if(key not in visited):
                dfs(key)
                res = res + 1

        return res
