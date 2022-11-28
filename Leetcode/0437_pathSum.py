# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        return self.count_paths_recursive(root, targetSum, [])
    
    def count_paths_recursive(self, currentNode, targetSum, currentPath):
        if currentNode is None:
            return 0
        
        currentPath.append(currentNode.val)
        pathCount, pathSum = 0, 0
        
        for i in range(len(currentPath)-1, -1, -1):
            pathSum += currentPath[i]
            if pathSum == targetSum:
                pathCount += 1
                
        pathCount += self.count_paths_recursive(currentNode.left, targetSum, currentPath)
        pathCount += self.count_paths_recursive(currentNode.right, targetSum, currentPath)
        
        del currentPath[-1]
        
        return pathCount