# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        


        queue = deque()

        queue.append(root)

        ans = []
        while queue:
            level = []
            for _ in range(len(queue)):
                pop = queue.popleft()
                level.append(pop.val)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            ans.append(level)
        return ans
        
            


        