# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result=[]
        queue=deque([root])
        left_right=True

        while queue:
            level=len(queue)

            level_node=deque()

            for i in range(level):
                node=queue.popleft()

                if left_right:
                    level_node.append(node.val)
                else:
                    level_node.appendleft(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            result.append(list(level_node))
            left_right = not left_right
        return result
