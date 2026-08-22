"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None


        copy  = Node(node.val)
        orgtocopy = {node: copy}


        def dfs(node):
            for x in node.neighbors:
                if(x not in orgtocopy):
                    orgtocopy[x] = Node(x.val)
                    dfs(x)
                    
                orgtocopy[node].neighbors.append(orgtocopy[x])

        dfs(node)

        return copy

        

                
