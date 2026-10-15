# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pre1 = []
        pre2 = []

        def dfs(node, pre):
            if not node:
                pre.append(None)
                return

            pre.append(node.val)
            dfs(node.left, pre)
            dfs(node.right, pre)
        

        dfs(p, pre1)
        dfs(q, pre2)

        return pre1 == pre2

            