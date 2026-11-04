# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced = True
        def dfs(node, level):
            nonlocal isBalanced
            if not node:
                return level

            left = dfs(node.left, level + 1) or 0
            right = dfs(node.right, level + 1) or 0

            if abs(left - right) > 1:
                isBalanced = False
            
            return max(left, right)
          
            
        dfs(root, 0)
        return isBalanced
                
            