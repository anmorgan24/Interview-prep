# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if root is None:
            return result
        
        queue = [(root)]
        
        while queue:
            levelSize = len(queue)
            currentLevel=[]
            
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                currentLevel.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.append(sum(currentLevel)/levelSize)
            
        return result