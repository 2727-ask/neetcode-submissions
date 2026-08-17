# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   


    def sameTree(self, p, q):
        if(p == None and q == None):
            return True

        if(p == None or q == None):
            return False

        if(p.val != q.val):
            return False


        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return False
            
            if(root.val == subRoot.val):
                if self.sameTree(root, subRoot) == True:
                    return True

            left = dfs(root.left)
            right = dfs(root.right)

            return left or right

        return dfs(root)

