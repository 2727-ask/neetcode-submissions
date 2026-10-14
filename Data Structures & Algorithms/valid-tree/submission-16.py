class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != n-1):
            return False
        visited = set()

        adjList = defaultdict(list)

        for node in range(n):
            adjList[node] = []

        for source, dest in edges:
            adjList[dest].append(source)
            adjList[source].append(dest)
        
        cycleDetected = False

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for child in adjList[node]:
                dfs(child)
            return True
        
        dfs(0)

        return n == len(visited)
                


