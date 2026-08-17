# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        while(len(queue) > 0):
            chunk = []
            for x in range(len(queue)):
                elm = queue.popleft()
                if(elm):
                    chunk.append(elm.val)
                    if(elm.left is not None):
                        queue.append(elm.left)
                    if(elm.right is not None):
                        queue.append(elm.right)
            if(chunk):
                ans.append(chunk)


        return ans


