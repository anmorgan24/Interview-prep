# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.find_root_to_leaf_path_numbers(root, 0)
    
    def find_root_to_leaf_path_numbers(self, currentNode, pathSum):
        
        if currentNode is None:
            return 0
        
        pathSum = 10 * pathSum + currentNode.val
        
        if currentNode.left is None and currentNode.right is None:
            return pathSum
        
        return self.find_root_to_leaf_path_numbers(currentNode.left, pathSum) + self.find_root_to_leaf_path_numbers(currentNode.right, pathSum)
        