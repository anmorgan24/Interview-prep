# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [(root)]
        maximumTreeDepth =0
        while queue:
            maximumTreeDepth += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.pop(0)
            
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return maximumTreeDepth