# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        

        queue = deque()

        queue.append((root, root.val))

        ans = 0

        while queue:
                pop, maximum = queue.popleft()
                if(pop.val >= maximum):
                    maximum = pop.val
                    ans = ans + 1
                if pop and pop.left:
                    queue.append((pop.left, maximum))
                if pop and pop.right:
                    queue.append((pop.right, maximum))
        
        return ans