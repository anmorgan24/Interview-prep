# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        allPaths = []
        self.find_paths_recursive(root, [], allPaths)
        
        return allPaths
    
    def find_paths_recursive(self, currentNode, currentPath, allPaths):
        if currentNode is None:
            return 
        
        currentPath.append(currentNode.val)
        
        if currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
            
        else:
            self.find_paths_recursive(currentNode.left, currentPath, allPaths)
            
            self.find_paths_recursive(currentNode.right, currentPath, allPaths)
            
        del currentPath[-1]