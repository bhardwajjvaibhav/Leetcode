# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        queue=deque([root])

        if not root:
            return []

        while queue:
            level=len(queue)

            for i in range(level):
                node=queue.popleft()

                if i==level-1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return result
        