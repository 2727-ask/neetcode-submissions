class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # {
        #     0: [1]
        #     1: [0, 2]
        #     2: [1]

        #     3: [4]
        #     4: [3]
        # }


        components = 1

        adjList = defaultdict(list)
        visited = set()

        for node in range(n):
            adjList[node] = []

        for source, dest in edges:
            adjList[source].append(dest)
            adjList[dest].append(source)

        
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for child in adjList[node]:
                    dfs(child)
        
        dfs(0)

        for source, dest in adjList.items():
            if(source not in visited):
                components = components + 1
                dfs(source)
        
        return components
        
        

        