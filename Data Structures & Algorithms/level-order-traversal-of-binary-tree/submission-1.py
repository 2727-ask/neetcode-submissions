# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return ans


        queue = deque()
        queue.append(root)

        path = []
        while queue:
            for x in range(len(queue)):
                pop = queue.popleft()
                path.append(pop.val)
                if(pop and pop.left):
                    queue.append(pop.left)
                if(pop and pop.right):
                    queue.append(pop.right)
            ans.append(path)
            path = []
                
            
        return ans
        



