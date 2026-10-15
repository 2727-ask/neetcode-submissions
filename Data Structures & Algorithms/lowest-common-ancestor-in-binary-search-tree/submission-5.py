# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        


        ans = None 


        def dfs(node):
            nonlocal ans 

            if not node:
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)

            self = 0
            if node == p or node == q:
                self = 1 
            
            mid = self + left + right 

            if(mid >= 2 and not ans):
                ans = node 
            
            return mid
        
        dfs(root)


        return ans