class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0


        def dfs(root):
            if(not root):
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal diameter
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        
        dfs(root)

        return diameter

        