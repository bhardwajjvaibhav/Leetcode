# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result=[]
        queue=deque([root])
        s=0
        avg=0

        if not root:
            return []

        while queue:
            level=len(queue)
            s=0
            avg=0

            for i in range(level):
                node=queue.popleft()
                s=s+node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            avg=s/level
            result.append(avg)
        return result  