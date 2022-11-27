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
        :rtype: List[List[int]]
        """
        allPaths = []
        self.find_paths_recursive(root, targetSum, [], allPaths)
        
        return allPaths
    
    def find_paths_recursive(self, currentNode, targetSum, currentPath, allPaths):
        if currentNode is None:
            return 
        
        currentPath.append(currentNode.val)
        
        if currentNode.val == targetSum and currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
            
        else:
            self.find_paths_recursive(currentNode.left, targetSum- currentNode.val, currentPath, allPaths)
            
            self.find_paths_recursive(currentNode.right, targetSum- currentNode.val, currentPath, allPaths)
            
        del currentPath[-1]