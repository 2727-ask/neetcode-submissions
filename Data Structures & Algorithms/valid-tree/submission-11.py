class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != n - 1):
            return False
            
        visited = set()
        adjList = defaultdict(list)

        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        count = 0
        def dfs(node, edge):
            nonlocal visited
            nonlocal count
            if(node in visited):
                return False
            count = count + 1
            visited.add(node)

            for child in adjList[node]:
                dfs(child, edge + 1)
            
            return True
       
        
        dfs(0, 0)
        print(count)
        return count == n


        

            
