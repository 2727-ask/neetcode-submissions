# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        n1 = []
        n2 = []

        def dfs(root, arr):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)

        dfs(p, n1)
        dfs(q, n2)

        return n1 == n2