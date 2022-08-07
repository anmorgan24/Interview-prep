# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        queue = [(root)]
        while queue:
            levelSize = len(queue)
            currentLevel = []
            
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                # add the node to the current level
                currentLevel.append(currentNode.val)
                # insert the children of the current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.insert(0, currentLevel)
            
        return result