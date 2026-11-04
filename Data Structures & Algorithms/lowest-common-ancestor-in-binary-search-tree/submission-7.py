# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        if root == p:
            return root 
        
        if root == q:
            return root

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
            
            sum = self + left + right
            if(sum >= 2 and ans is None):
                ans = node

            return sum
        
        dfs(root)
        return ans
            

