# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        

        queue = deque()

        queue.append(root)

        ans = []
        while queue:
            chunk = []
            for _ in range(len(queue)):
                pop = queue.popleft()
                chunk.append(pop)
                if(pop and pop.left):
                    queue.append(pop.left)
                if(pop and pop.right):
                    queue.append(pop.right)
            if(chunk):
                ans.append(chunk[-1].val)
        
        return ans
                

            



        