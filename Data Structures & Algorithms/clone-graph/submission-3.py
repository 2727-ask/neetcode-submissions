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


        copy = Node(node.val)
        orgtonew = {node: copy}


        def dfs(node):
            for x in node.neighbors:
                if(x not in orgtonew):
                    orgtonew[x] = Node(x.val)
                    dfs(x)
                
                orgtonew[node].neighbors.append(orgtonew[x])

        dfs(node)

        return copy



        

                
