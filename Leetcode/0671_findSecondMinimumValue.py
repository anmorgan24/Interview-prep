# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = []
        if root is None:
            return -1
        
        queue = [(root)]
        while queue:
            levelSize = len(queue)
            currentLevel = []
            
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                currentLevel.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            
            result.extend(currentLevel)
            result = list(set(result))
            
        result.remove(min(result))    
        if len(result)>0:
            return min(result)
        else:
            return -1